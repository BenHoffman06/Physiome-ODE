from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pandas as pd


def sanitize_name(name: str) -> str:
    """
    Make a filesystem-safe name.
    """
    if pd.isna(name):
        return "unknown"

    name = str(name).strip()
    name = re.sub(r"[^\w\-. ]+", "_", name)
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_+", "_", name).strip("._")
    return name or "unknown"


def make_unique_dir(base_dir: Path) -> Path:
    """
    Avoid collisions if a folder already exists.
    """
    if not base_dir.exists():
        return base_dir

    counter = 2
    while True:
        candidate = base_dir.parent / f"{base_dir.name}_{counter}"
        if not candidate.exists():
            return candidate
        counter += 1


def run_command(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )


def write_text(path: Path, text: str) -> None:
    path.write_text(text if text is not None else "", encoding="utf-8")


def process_models(
    csv_path: str | Path,
    output_root: str | Path,
    opencor_exe: str,
    summary_csv: str | Path = "cellml_export_summary.csv",
    skip_existing_success: bool = True,
) -> pd.DataFrame:
    """
    Expected CSV columns:
    Model Name, File, Domain, All Domains, Equation Count,
    Differential Equation Count, Algebraic Equation Count,
    ODE count, PDE count, State variable count,
    Algebraic Variable Count, Total Variable Count, Actual Variable Count
    """
    csv_path = Path(csv_path)
    output_root = Path(output_root)
    summary_csv = Path(summary_csv)

    output_root.mkdir(parents=True, exist_ok=True)
    results = []

    df = pd.read_csv(csv_path)

    required_cols = ["Model Name", "File", "Domain"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Missing required columns: {missing_cols}. "
            f"Found columns: {list(df.columns)}"
        )

    for idx, row in df.iterrows():
        model_name_raw = row["Model Name"]
        file_raw = row["File"]
        domain_raw = row["Domain"]

        record = {
            "row_index": idx,
            "model_name_raw": model_name_raw,
            "file_raw": file_raw,
            "domain_raw": domain_raw,
            "model_name": None,
            "domain": None,
            "output_dir": None,
            "copied_cellml": None,
            "validate_returncode": None,
            "validate_stdout": None,
            "validate_stderr": None,
            "export_returncode": None,
            "export_stdout": None,
            "export_stderr": None,
            "status": None,
        }

        try:
            if pd.isna(file_raw) or not str(file_raw).strip():
                record["status"] = "missing_source"
                results.append(record)
                continue

            src = Path(str(file_raw)).expanduser().resolve()
            if not src.exists():
                record["status"] = "missing_source"
                results.append(record)
                continue

            model_name = sanitize_name(model_name_raw)
            domain = sanitize_name(domain_raw)

            base_model_dir = output_root / domain / model_name
            model_dir = make_unique_dir(base_model_dir)
            model_dir.mkdir(parents=True, exist_ok=True)

            copied_cellml = model_dir / src.name
            shutil.copy2(src, copied_cellml)

            record["model_name"] = model_name
            record["domain"] = domain
            record["output_dir"] = str(model_dir)
            record["copied_cellml"] = str(copied_cellml)

            success_marker = model_dir / "EXPORT_SUCCESS.txt"
            if skip_existing_success and success_marker.exists():
                record["status"] = "success"
                results.append(record)
                continue

            # Validate
            validate_cmd = [
                opencor_exe,
                "-c",
                "CellMLTools::validate",
                str(copied_cellml.name),
            ]
            val = run_command(validate_cmd, cwd=model_dir)

            record["validate_returncode"] = val.returncode
            record["validate_stdout"] = val.stdout
            record["validate_stderr"] = val.stderr

            write_text(model_dir / "validate_stdout.txt", val.stdout)
            write_text(model_dir / "validate_stderr.txt", val.stderr)

            if val.returncode != 0:
                record["status"] = "validation_failed"
                results.append(record)
                continue

            # Export to Python
            export_cmd = [
                opencor_exe,
                "-c",
                "CellMLTools::export",
                str(copied_cellml.name),
                "python",
            ]
            exp = run_command(export_cmd, cwd=model_dir)

            record["export_returncode"] = exp.returncode
            record["export_stdout"] = exp.stdout
            record["export_stderr"] = exp.stderr

            write_text(model_dir / "export_stdout.txt", exp.stdout)
            write_text(model_dir / "export_stderr.txt", exp.stderr)

            # Optional sanity check: did a .py file appear?
            py_files = list(model_dir.glob("*.py"))
            record["generated_py_files"] = " | ".join(str(p.name) for p in py_files)

            if exp.returncode != 0:
                record["status"] = "export_failed"
                results.append(record)
                continue

            success_marker.write_text("success\n", encoding="utf-8")
            record["status"] = "success"
            results.append(record)

        except Exception as e:
            record["status"] = "exception"
            record["export_stderr"] = str(e)
            results.append(record)

    result_df = pd.DataFrame(results)
    result_df.to_csv(summary_csv, index=False)
    return result_df


if __name__ == "__main__":
    result_df = process_models(
        csv_path="CellML_model_list_only_ODE.csv",
        output_root="exported_cellml_models",
        opencor_exe="/Applications/OpenCOR/OpenCOR",  # macOS example
        summary_csv="cellml_export_summary.csv",
    )

    print(result_df["status"].value_counts(dropna=False))