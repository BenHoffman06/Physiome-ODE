#simulate_sbml.py
"""
A minimal standalone example for simulating one SBML model with Tellurium.

Examples
--------
Use a model already stored in SysBio-Traj/Data:
python simulate_sbml.py \
  --model-id BIOMD0000000013 \
  --model-name Poolman2004 \
  --start-time 0 \
  --end-time 0.4 \
  --num-timepoints 512

Use the initial_conditions.json file in the same model directory:
python simulate_sbml.py \
  --model-id BIOMD0000000013 \
  --model-name Poolman2004 \
  --start-time 0 \
  --end-time 0.4 \
  --num-timepoints 512 \
  --use-ic-json \
  --output scripts/BIOMD0000000013_Poolman2004_simulated.csv

Use a custom SBML file directly:
python simulate_sbml.py \
  --xml-file /path/to/model.xml \
  --start-time 0 \
  --end-time 100 \
  --num-timepoints 512 \
  --output /path/to/output.csv
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import tellurium as te


ROOT_DIR = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulate one SBML model.")

    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument(
        "--xml-file",
        type=Path,
        help="Path to an SBML XML file.",
    )
    source_group.add_argument(
        "--model-id",
        help="Model ID under SysBio-Traj/Data, for example BIOMD0000000013.",
    )

    parser.add_argument(
        "--model-name",
        help="Model name used to resolve Data/<model_id>/<model_name>.xml.",
    )
    parser.add_argument("--start-time", type=float, required=True, help="Simulation start time.")
    parser.add_argument("--end-time", type=float, required=True, help="Simulation end time.")
    parser.add_argument(
        "--num-timepoints",
        type=int,
        default=512,
        help="Number of sampled time points.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output CSV path. If omitted, the file is saved in the scripts directory.",
    )
    parser.add_argument(
        "--ic-json",
        type=Path,
        default=None,
        help="Path to a JSON file containing initial conditions.",
    )
    parser.add_argument(
        "--use-ic-json",
        action="store_true",
        help="Use Data/<model_id>/initial_conditions.json.",
    )
    return parser.parse_args()


def resolve_xml_path(args: argparse.Namespace) -> Path:
    if args.xml_file is not None:
        return args.xml_file.resolve()

    if not args.model_name:
        raise ValueError("--model-name is required when --model-id is used.")

    xml_path = ROOT_DIR / "Data" / args.model_id / f"{args.model_name}.xml"
    return xml_path.resolve()


def resolve_output_path(args: argparse.Namespace, xml_path: Path) -> Path:
    if args.output is not None:
        return args.output.resolve()

    if args.model_id and args.model_name:
        filename = f"{args.model_id}_{args.model_name}_simulated.csv"
    else:
        filename = f"{xml_path.stem}_simulated.csv"

    return (ROOT_DIR / "scripts" / filename).resolve()


def resolve_ic_json_path(args: argparse.Namespace) -> Path | None:
    if args.ic_json is not None:
        return args.ic_json.resolve()

    if args.use_ic_json:
        if not args.model_id:
            raise ValueError("--use-ic-json can only be used together with --model-id.")
        return (ROOT_DIR / "Data" / args.model_id / "initial_conditions.json").resolve()

    return None


def load_initial_conditions(ic_json_path: Path | None) -> dict[str, float]:
    if ic_json_path is None:
        return {}

    with ic_json_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    if isinstance(payload, dict) and "initial_conditions" in payload:
        payload = payload["initial_conditions"]

    if not isinstance(payload, dict):
        raise ValueError(f"Initial-condition JSON must be a dictionary: {ic_json_path}")

    ic_map: dict[str, float] = {}
    for key, value in payload.items():
        if value is None:
            continue
        ic_map[str(key)] = float(value)
    return ic_map


def set_model_value(rr, name: str, value: float) -> bool:
    candidates = []
    stripped = name.strip()
    bare = stripped[1:-1] if stripped.startswith("[") and stripped.endswith("]") else stripped

    for candidate in (stripped, bare, f"[{bare}]"):
        if candidate not in candidates:
            candidates.append(candidate)

    for candidate in candidates:
        try:
            rr[candidate] = float(value)
            return True
        except Exception:
            continue

    return False


def apply_initial_conditions(rr, ic_map: dict[str, float]) -> None:
    for name, value in ic_map.items():
        ok = set_model_value(rr, name, value)
        if not ok:
            print(f"Warning: cannot set initial condition for '{name}', skipped.")


def normalize_column_name(name: str) -> str:
    text = str(name).strip()
    if text.startswith("[") and text.endswith("]"):
        return text[1:-1]
    return text


def simulate_sbml(
    xml_path: Path,
    output_path: Path,
    start_time: float,
    end_time: float,
    num_timepoints: int,
    ic_json_path: Path | None = None,
) -> Path:
    rr = te.loadSBMLModel(str(xml_path))

    ic_map = load_initial_conditions(ic_json_path)
    if ic_map:
        apply_initial_conditions(rr, ic_map)

    result = rr.simulate(start_time, end_time, num_timepoints)
    columns = [normalize_column_name(name) for name in result.colnames]
    df = pd.DataFrame(np.asarray(result), columns=columns)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path


def main() -> None:
    args = parse_args()
    xml_path = resolve_xml_path(args)
    output_path = resolve_output_path(args, xml_path)
    ic_json_path = resolve_ic_json_path(args)

    if not xml_path.is_file():
        raise FileNotFoundError(f"Cannot find SBML file: {xml_path}")
    if ic_json_path is not None and not ic_json_path.is_file():
        raise FileNotFoundError(f"Cannot find IC JSON file: {ic_json_path}")

    saved_path = simulate_sbml(
        xml_path=xml_path,
        output_path=output_path,
        start_time=args.start_time,
        end_time=args.end_time,
        num_timepoints=args.num_timepoints,
        ic_json_path=ic_json_path,
    )
    print(f"Saved to: {saved_path}")


if __name__ == "__main__":
    main()