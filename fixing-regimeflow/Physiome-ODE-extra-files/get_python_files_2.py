from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pandas as pd


def sanitize_name(name: str) -> str:
    if pd.isna(name):
        return "unknown"

    name = str(name).strip()
    name = re.sub(r"[^\w\-. ]+", "_", name)
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_+", "_", name).strip("._")
    return name or "unknown"


def make_unique_dir(base_dir: Path) -> Path:
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
    path.write_text(
        text if text is not None else "",
        encoding="utf-8",
        errors="replace",
    )


def extract_python_code(text: str) -> str:
    """
    OpenCOR may print diagnostics before the actual Python code.
    This extracts from the first Python-looking line onward.
    """
    lines = text.splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if (
            stripped.startswith("from ")
            or stripped.startswith("import ")
            or stripped.startswith("def ")
            or stripped.startswith("#")
        ):
            start_idx = i
            break

    if start_idx is None:
        return ""

    return "\n".join(lines[start_idx:]).strip() + "\n"


def extract_undefined_variables(text: str) -> str:
    """
    Pull out the variable names listed after:
    'The following variables couldn't be defined:'
    """
    lines = text.splitlines()
    capture = False
    vars_list = []

    for line in lines:
        if "The following variables couldn't be defined" in line:
            capture = True
            continue

        if capture:
            stripped = line.strip()
            if not stripped:
                break
            vars_list.append(stripped)

    return " | ".join(vars_list)


def process_models(
    csv_path: str | Path,
    output_root: str | Path,
    opencor_exe: str,
    summary_csv: str | Path = "cellml_export_summary.csv",
    skip_existing_success: bool = False,
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
            "generated_py_file": None,
            "generated_py_size": 0,
            "validate_returncode": None,
            "export_returncode": None,
            "underconstrained": False,
            "undefined_variables": "",
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
                record["status"] = "success_clean"
                results.append(record)
                continue

            local_name = copied_cellml.name

            # Validate
            validate_cmd = [
                opencor_exe,
                "-c",
                "CellMLTools::validate",
                local_name,
            ]
            val = run_command(validate_cmd, cwd=model_dir)

            record["validate_returncode"] = val.returncode

            write_text(model_dir / "validate_stdout.txt", val.stdout)
            write_text(model_dir / "validate_stderr.txt", val.stderr)

            if val.returncode != 0:
                record["status"] = "validation_failed"
                results.append(record)
                continue

            # Export
            export_cmd = [
                opencor_exe,
                "-c",
                "CellMLTools::export",
                local_name,
                "python",
            ]
            exp = run_command(export_cmd, cwd=model_dir)

            record["export_returncode"] = exp.returncode

            write_text(model_dir / "export_stdout_raw.txt", exp.stdout)
            write_text(model_dir / "export_stderr.txt", exp.stderr)

            stdout_text = exp.stdout or ""
            stderr_text = exp.stderr or ""

            has_underconstrained = (
                "Model is underconstrained" in stdout_text
                or "The following variables couldn't be defined" in stdout_text
                or "Model is underconstrained" in stderr_text
                or "The following variables couldn't be defined" in stderr_text
            )

            record["underconstrained"] = has_underconstrained
            record["undefined_variables"] = extract_undefined_variables(stdout_text)

            if has_underconstrained:
                write_text(
                    model_dir / "underconstrained_report.txt",
                    stdout_text,
                )

            python_code = extract_python_code(stdout_text)
            py_path = model_dir / f"{copied_cellml.stem}.py"

            if python_code:
                write_text(py_path, python_code)
                record["generated_py_file"] = str(py_path)
                record["generated_py_size"] = py_path.stat().st_size

            if exp.returncode != 0:
                record["status"] = "export_failed"
            elif not python_code:
                record["status"] = "export_failed"
            elif has_underconstrained:
                record["status"] = "success_underconstrained"
            else:
                success_marker.write_text("success\n", encoding="utf-8")
                record["status"] = "success_clean"

            results.append(record)

        except Exception as e:
            record["status"] = "exception"
            write_text(
                output_root / "last_exception.txt",
                f"Row {idx}\n{repr(e)}\n",
            )
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