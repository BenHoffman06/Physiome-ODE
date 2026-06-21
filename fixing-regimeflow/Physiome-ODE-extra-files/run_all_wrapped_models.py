from __future__ import annotations

import argparse
import csv
import importlib.util
import inspect
import json
import sys
from pathlib import Path


def load_module_from_path(module_path: str | Path):
    module_path = Path(module_path).resolve()
    module_name = module_path.stem

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def find_wrapped_model_files(root: str | Path) -> list[Path]:
    root = Path(root)
    return sorted(root.rglob("*_wrapped.py"))


def load_parameters(module, model_dir: Path, conditions_name: str | None):
    """
    Load Parameters either from defaults or from a JSON file in the model directory.

    conditions_name examples:
      None                    -> use default Parameters()
      "custom"                -> load model_dir/custom.json
      "custom.json"           -> load model_dir/custom.json
      "{model}_conditions"    -> load model_dir/{model}_conditions.json
    """
    if not hasattr(module, "Parameters"):
        raise AttributeError("Module does not define Parameters")

    if conditions_name is None:
        return module.Parameters()

    json_name = conditions_name if conditions_name.endswith(".json") else f"{conditions_name}.json"
    json_path = model_dir / json_name

    if not json_path.exists():
        raise FileNotFoundError(f"Conditions file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if hasattr(module.Parameters, "from_dict"):
        return module.Parameters.from_dict(data)

    p = module.Parameters()
    for key, value in data.items():
        if hasattr(p, key):
            setattr(p, key, value)
    return p


def get_default_t_unit(config_cls) -> float:
    """
    Read default T_unit from Config.__init__ if available.
    Falls back to 0.01.
    """
    default_t_unit = 0.01
    try:
        sig = inspect.signature(config_cls.__init__)
        if "T_unit" in sig.parameters:
            default_val = sig.parameters["T_unit"].default
            if isinstance(default_val, (int, float)):
                default_t_unit = float(default_val)
    except Exception:
        pass
    return default_t_unit


def export_config_to_csv(config, output_csv: str | Path) -> Path:
    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    if config.truth is None:
        raise ValueError("Config.truth is None. Run with calculate=True.")

    header = ["t"] + list(config.curve_names)

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i, t in enumerate(config.t):
            writer.writerow([t] + list(config.truth[i]))

    return output_csv


def run_single_model(
    wrapped_model_file: str | Path,
    n_steps: int = 1000,
    conditions_name: str | None = None,
) -> Path:
    wrapped_model_file = Path(wrapped_model_file).resolve()
    model_dir = wrapped_model_file.parent
    module = load_module_from_path(wrapped_model_file)

    if not hasattr(module, "Config"):
        raise AttributeError(f"{wrapped_model_file} does not define Config")
    if not hasattr(module, "Parameters"):
        raise AttributeError(f"{wrapped_model_file} does not define Parameters")

    params = load_parameters(
        module=module,
        model_dir=model_dir,
        conditions_name=conditions_name,
    )

    T_unit = get_default_t_unit(module.Config)
    T = n_steps * T_unit

    config = module.Config(
        param=params,
        calculate=True,
        T=T,
        T_unit=T_unit,
    )

    model_base = wrapped_model_file.stem.replace("_wrapped", "")
    output_csv = model_dir / f"{model_base}.csv"
    return export_config_to_csv(config, output_csv)


def batch_run_models(
    wrapped_root: str | Path,
    n_steps: int = 1000,
    conditions_name: str | None = None,
) -> tuple[list[dict], list[dict]]:
    wrapped_root = Path(wrapped_root)
    wrapped_files = find_wrapped_model_files(wrapped_root)

    success = []
    failed = []

    for wrapped_file in wrapped_files:
        try:
            output_csv = run_single_model(
                wrapped_model_file=wrapped_file,
                n_steps=n_steps,
                conditions_name=conditions_name,
            )
            success.append(
                {
                    "wrapped_model_file": str(wrapped_file),
                    "output_csv": str(output_csv),
                    "status": "ok",
                    "detail": "",
                }
            )
            print(f"[OK] {wrapped_file.name} -> {output_csv.name}")
        except Exception as e:
            failed.append(
                {
                    "wrapped_model_file": str(wrapped_file),
                    "output_csv": "",
                    "status": "failed",
                    "detail": str(e),
                }
            )
            print(f"[FAIL] {wrapped_file.name}: {e}")

    return success, failed


def write_summary(success: list[dict], failed: list[dict], output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = success + failed
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["wrapped_model_file", "output_csv", "status", "detail"],
        )
        writer.writeheader()
        writer.writerows(rows)

    return output_path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch-run wrapped CellML models and export CSV results."
    )
    parser.add_argument(
        "--wrapped-root",
        type=str,
        default="wrapped_models",
        help="Root directory containing wrapped model folders. Default: wrapped_models",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=1000,
        help="Number of time steps to run. Default: 1000",
    )
    parser.add_argument(
        "--conditions-name",
        type=str,
        default=None,
        help=(
            "Name of a JSON file in each model directory, with or without .json. "
            "If omitted, uses default model Parameters()."
        ),
    )
    parser.add_argument(
        "--summary-name",
        type=str,
        default="batch_run_results.csv",
        help="Filename for the batch summary CSV written under wrapped_root.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    wrapped_root = Path(args.wrapped_root).resolve()

    success, failed = batch_run_models(
        wrapped_root=wrapped_root,
        n_steps=args.steps,
        conditions_name=args.conditions_name,
    )

    summary_csv = wrapped_root / args.summary_name
    write_summary(success, failed, summary_csv)

    print(f"\nProcessed: {len(success) + len(failed)}")
    print(f"Succeeded: {len(success)}")
    print(f"Failed: {len(failed)}")
    print(f"Summary written to: {summary_csv}")


if __name__ == "__main__":
    main()