from __future__ import annotations

import ast
import json
import re
import shutil
from pathlib import Path

import pandas as pd


WRAPPER_MARKER = "# =========================\n# Auto-generated wrapper\n# =========================\n"


# def sanitize_name(name: str) -> str:
#     """
#     Convert a legend-derived name into a valid Python identifier.
#     """
#     name = name.strip()
#     name = name.split(" in component ")[0].strip()
#     name = re.sub(r"[^0-9a-zA-Z_]", "_", name)
#     name = re.sub(r"_+", "_", name).strip("_")

#     if not name:
#         name = "unnamed"
#     if name[0].isdigit():
#         name = f"var_{name}"

#     return name

def sanitize_name(name: str) -> str:
    name = name.strip()
    name = name.split(" in component ")[0].strip()
    name = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    name = re.sub(r"_+", "_", name)

    # remove leading underscores, but preserve trailing ones
    name = name.lstrip("_")

    if not name:
        name = "unnamed"
    if name[0].isdigit():
        name = f"var_{name}"
    return name

def uniquify_indexed_names(names: dict[int, str]) -> dict[int, str]:
    used = {}
    out = {}

    for idx in sorted(names):
        base = names[idx]
        if base not in used:
            used[base] = 1
            out[idx] = base
        else:
            suffix = used[base]
            candidate = f"{base}_{suffix}"
            while candidate in used:
                suffix += 1
                candidate = f"{base}_{suffix}"
            used[base] += 1
            used[candidate] = 1
            out[idx] = candidate

    return out

def make_safe_filename(name: str) -> str:
    """
    Safe filename for output files/folders.
    """
    return "".join(ch if ch.isalnum() or ch in ("_", "-", ".") else "_" for ch in name)


def extract_size(text: str, var_name: str) -> int:
    m = re.search(rf"^\s*{re.escape(var_name)}\s*=\s*(\d+)", text, flags=re.MULTILINE)
    if not m:
        raise ValueError(f"Could not find {var_name}")
    return int(m.group(1))


def get_top_level_function_node(text: str, func_name: str):
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
    raise ValueError(f"Could not find function {func_name}")


def extract_function_source(text: str, func_name: str) -> str:
    node = get_top_level_function_node(text, func_name)
    lines = text.splitlines(keepends=True)
    return "".join(lines[node.lineno - 1 : node.end_lineno])


def extract_subscript_index(target: ast.Subscript) -> int:
    sl = target.slice

    if isinstance(sl, ast.Constant) and isinstance(sl.value, int):
        return sl.value

    # compatibility branch
    if hasattr(ast, "Index") and isinstance(sl, ast.Index):
        if isinstance(sl.value, ast.Constant) and isinstance(sl.value.value, int):
            return sl.value.value

    raise ValueError("Unsupported subscript index")


def extract_legend_names(text: str, array_name: str, size: int) -> dict[int, str]:
    """
    Extract names from legend_constants / legend_states / legend_algebraic.
    """
    pattern = re.compile(rf'{array_name}\[(\d+)\]\s*=\s*"([^"]+)"')
    names: dict[int, str] = {}

    for idx_s, raw in pattern.findall(text):
        idx = int(idx_s)
        if 0 <= idx < size:
            names[idx] = sanitize_name(raw)

    for i in range(size):
        names.setdefault(i, f"{array_name}_{i}")

    return names


def extract_init_consts_info(text: str):
    """
    Parse initConsts() and return:
      direct_constants: {idx: rhs}
      derived_constants: {idx: rhs}
      state_assignments: {idx: rhs}
    """
    func_src = extract_function_source(text, "initConsts")
    tree = ast.parse(func_src)
    func = tree.body[0]

    direct_constants: dict[int, str] = {}
    derived_constants: dict[int, str] = {}
    state_assignments: dict[int, str] = {}

    for node in ast.walk(func):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue

        target = node.targets[0]
        rhs = ast.get_source_segment(func_src, node.value)
        if rhs is None:
            continue
        rhs = rhs.strip()

        if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
            arr_name = target.value.id
            idx = extract_subscript_index(target)

            if arr_name == "constants":
                if "constants[" in rhs:
                    derived_constants[idx] = rhs
                else:
                    direct_constants[idx] = rhs
            elif arr_name == "states":
                state_assignments[idx] = rhs

    return direct_constants, derived_constants, state_assignments


def split_top_level_csv(s: str) -> list[str]:
    """
    Split a comma-separated string while respecting parentheses/brackets.
    """
    out = []
    cur = []
    depth = 0

    for ch in s:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1

        if ch == "," and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)

    if cur:
        out.append("".join(cur).strip())

    return out


def convert_condition(cond: str) -> str:
    cond = cond.strip()

    if cond == "True":
        return "True"

    m = re.fullmatch(r"less\((.*?),(.*)\)", cond)
    if m:
        return f"({m.group(1).strip()} < {m.group(2).strip()})"

    m = re.fullmatch(r"greater\((.*?),(.*)\)", cond)
    if m:
        return f"({m.group(1).strip()} > {m.group(2).strip()})"

    return cond


def convert_custom_piecewise(expr: str) -> str:
    """
    Convert simple custom_piecewise([...]) forms from initConsts().
    """
    m = re.fullmatch(r"custom_piecewise\(\[(.*)\]\)", expr.strip())
    if not m:
        return expr

    parts = split_top_level_csv(m.group(1).strip())
    if len(parts) != 4:
        return expr

    cond1, val1, cond2, val2 = [p.strip() for p in parts]
    cond1 = convert_condition(cond1)
    cond2 = convert_condition(cond2)

    if cond2 == "True":
        return f"({val1} if {cond1} else {val2})"

    return f"({val1} if {cond1} else ({val2} if {cond2} else None))"


def convert_expr(expr: str) -> str:
    """
    Conservative conversion for derived constant expressions.
    """
    return convert_custom_piecewise(expr)


def generate_parameters_block(
    size_constants: int,
    constant_names: dict[int, str],
    direct_constants: dict[int, str],
) -> str:
    init_lines = ["class Parameters:", "    def __init__(self):"]
    wrote_any = False

    for i in range(size_constants):
        if i in direct_constants:
            init_lines.append(f"        self.{constant_names[i]} = {direct_constants[i]}")
            wrote_any = True

    if not wrote_any:
        init_lines.append("        pass")

    dict_lines = ["", "    def to_dict(self):", "        return {"]
    for i in range(size_constants):
        if i in direct_constants:
            dict_lines.append(f'            "{constant_names[i]}": self.{constant_names[i]},')
    dict_lines.append("        }")

    from_dict_lines = [
        "",
        "    @classmethod",
        "    def from_dict(cls, data):",
        "        p = cls()",
        "        for key, value in data.items():",
        "            if hasattr(p, key):",
        "                setattr(p, key, value)",
        "        return p",
    ]

    return "\n".join(init_lines + dict_lines + from_dict_lines)


def generate_curve_names_block(state_names: dict[int, str]) -> str:
    curve_names = [state_names[i] for i in sorted(state_names)]

    lines = ["        self.curve_names = ["]
    for name in curve_names:
        lines.append(f'            "{name}",')
    lines.append("        ]")

    return "\n".join(lines)


def generate_y0_default_text(size_states: int, state_assignments: dict[int, str]) -> str:
    vals = [state_assignments.get(i, "0.0") for i in range(size_states)]
    return "[" + ", ".join(vals) + "]"


def generate_build_constants_block(
    size_constants: int,
    constant_names: dict[int, str],
    direct_constants: dict[int, str],
    derived_constants: dict[int, str],
) -> str:
    lines = [
        "    def _build_constants(self):",
        f"        c = [0.0] * {size_constants}",
        "        p = self.params",
        "",
        "        # direct mapping",
    ]

    for i in range(size_constants):
        if i in direct_constants:
            lines.append(f"        c[{i}] = p.{constant_names[i]}")

    if derived_constants:
        lines.extend(["", "        # derived constants"])
        for i in sorted(derived_constants):
            rhs = convert_expr(derived_constants[i])
            rhs = re.sub(r"constants\[(\d+)\]", r"c[\1]", rhs)
            lines.append(f"        c[{i}] = {rhs}")

    lines.extend([
        "",
        "        return np.asarray(c, dtype=float)",
    ])

    return "\n".join(lines)


# === New helper functions for conditions JSON ===

def parse_jsonable_value(expr: str):
    """
    Parse a simple Python literal/expression into a JSON-friendly value.
    Falls back to the original string if literal evaluation fails.
    """
    try:
        return ast.literal_eval(expr)
    except Exception:
        return expr


def build_conditions_dict(text: str) -> dict[str, object]:
    """
    Build a default conditions dictionary from direct constant assignments.
    """
    size_constants = extract_size(text, "sizeConstants")
    constant_names = extract_legend_names(text, "legend_constants", size_constants)
    constant_names = uniquify_indexed_names(constant_names)
    direct_constants, _, _ = extract_init_consts_info(text)

    conditions = {}
    for i in range(size_constants):
        if i in direct_constants:
            conditions[constant_names[i]] = parse_jsonable_value(direct_constants[i])

    return conditions


def write_conditions_json(
    text: str,
    output_dir: str | Path,
    model_base_name: str,
) -> Path:
    """
    Write a {model}_conditions.json file using direct constant assignments.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    conditions = build_conditions_dict(text)
    output_json = output_dir / f"{model_base_name}_conditions.json"

    with output_json.open("w", encoding="utf-8") as f:
        json.dump(conditions, f, indent=2, sort_keys=True)

    return output_json


def build_wrapper_text(text: str, model_name: str) -> str:
    size_states = extract_size(text, "sizeStates")
    size_algebraic = extract_size(text, "sizeAlgebraic")
    size_constants = extract_size(text, "sizeConstants")

    # constant_names = extract_legend_names(text, "legend_constants", size_constants)
    # state_names = extract_legend_names(text, "legend_states", size_states)
    # algebraic_names = extract_legend_names(text, "legend_algebraic", size_algebraic)

    constant_names = extract_legend_names(text, "legend_constants", size_constants)
    constant_names = uniquify_indexed_names(constant_names)

    state_names = extract_legend_names(text, "legend_states", size_states)
    state_names = uniquify_indexed_names(state_names)

    algebraic_names = extract_legend_names(text, "legend_algebraic", size_algebraic)
    algebraic_names = uniquify_indexed_names(algebraic_names)

    direct_constants, derived_constants, state_assignments = extract_init_consts_info(text)

    parameters_block = generate_parameters_block(
        size_constants=size_constants,
        constant_names=constant_names,
        direct_constants=direct_constants,
    )
    curve_names_block = generate_curve_names_block(state_names)
    y0_default = generate_y0_default_text(size_states, state_assignments)
    build_constants_block = generate_build_constants_block(
        size_constants=size_constants,
        constant_names=constant_names,
        direct_constants=direct_constants,
        derived_constants=derived_constants,
    )

    state_names_list = [state_names[i] for i in sorted(state_names)]
    algebraic_names_list = [algebraic_names[i] for i in sorted(algebraic_names)]

    wrapper = f"""
{WRAPPER_MARKER}import numpy as np
from scipy.integrate import odeint


{parameters_block}


class Config:
    def __init__(
        self,
        param: Parameters = None,
        calculate: bool = False,
        T: int = 100,
        T_unit: float = 0.01,
        y0={y0_default},
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "{model_name}"
{curve_names_block}
        self.state_names = {state_names_list}
        self.algebraic_names = {algebraic_names_list}
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

{build_constants_block}

    def pend(self, y, t):
        constants = self._build_constants()
        return np.asarray(
            computeRates(t, list(np.asarray(y, dtype=float)), constants),
            dtype=float,
        )

    def algebraic(self, y, t=0.0):
        if "computeAlgebraic" not in globals():
            raise AttributeError("computeAlgebraic is not defined in this module")

        alg = computeAlgebraic(
            self._build_constants(),
            np.asarray(y, dtype=float).reshape(-1, 1),
            np.asarray([t], dtype=float),
        )
        return np.asarray(alg, dtype=float)[:, 0]
"""
    return wrapper.strip() + "\n"


def append_wrapper_to_text(text: str, model_name: str) -> str:
    if WRAPPER_MARKER in text:
        raise ValueError("Wrapper already appended.")
    wrapper = build_wrapper_text(text=text, model_name=model_name)
    return text.rstrip() + "\n\n\n" + wrapper


def copy_matching_cellml_file(
    generated_py_file: str | Path,
    wrapped_output_dir: str | Path,
) -> Path | None:
    """
    Copy the sibling .cellml file into the wrapped output directory,
    preserving the original .cellml filename.
    """
    generated_py_file = Path(generated_py_file)
    wrapped_output_dir = Path(wrapped_output_dir)

    source_cellml = generated_py_file.with_suffix(".cellml")
    if not source_cellml.exists():
        return None

    wrapped_output_dir.mkdir(parents=True, exist_ok=True)
    dest_cellml = wrapped_output_dir / source_cellml.name
    shutil.copy2(source_cellml, dest_cellml)
    return dest_cellml


def wrap_single_generated_file(
    generated_py_file: str | Path,
    wrapped_output_file: str | Path,
    model_name: str | None = None,
    copy_cellml: bool = True,
    write_conditions: bool = True,
) -> tuple[Path, Path | None, Path | None]:
    generated_py_file = Path(generated_py_file)
    wrapped_output_file = Path(wrapped_output_file)
    wrapped_output_file.parent.mkdir(parents=True, exist_ok=True)

    text = generated_py_file.read_text(encoding="utf-8")
    wrapped_text = append_wrapper_to_text(
        text=text,
        model_name=model_name or generated_py_file.stem,
    )
    wrapped_output_file.write_text(wrapped_text, encoding="utf-8")

    copied_cellml = None
    if copy_cellml:
        copied_cellml = copy_matching_cellml_file(
            generated_py_file=generated_py_file,
            wrapped_output_dir=wrapped_output_file.parent,
        )

    conditions_json = None
    if write_conditions:
        conditions_json = write_conditions_json(
            text=text,
            output_dir=wrapped_output_file.parent,
            model_base_name=generated_py_file.stem,
        )

    return wrapped_output_file, copied_cellml, conditions_json


def batch_wrap_from_summary(
    summary_csv: str | Path,
    wrapped_root: str | Path,
    require_success_clean: bool = True,
    skip_underconstrained: bool = True,
    overwrite: bool = False,
    copy_cellml: bool = True,
    write_conditions: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Batch-wrap generated Python files listed in the export summary CSV.

    Output layout:
        wrapped_root/<domain>/<model_name>/<model_name>_wrapped.py
        wrapped_root/<domain>/<model_name>/<original_cellml_filename>.cellml
        wrapped_root/<domain>/<model_name>/<original_python_stem>_conditions.json
    """
    summary_csv = Path(summary_csv)
    wrapped_root = Path(wrapped_root)
    wrapped_root.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(summary_csv)

    for col in ["generated_py_file", "status", "domain", "model_name", "underconstrained"]:
        if col in df.columns:
            df[col] = df[col].fillna("")

    mask = df["generated_py_file"].astype(str).str.strip() != ""

    if require_success_clean and "status" in df.columns:
        mask &= df["status"].astype(str) == "success_clean"

    if skip_underconstrained and "underconstrained" in df.columns:
        under = df["underconstrained"].astype(str).str.lower()
        mask &= ~under.isin(["true", "1", "yes"])

    todo = df.loc[mask].copy()

    success_rows: list[dict] = []
    failed_rows: list[dict] = []

    for _, row in todo.iterrows():
        generated_py = Path(str(row["generated_py_file"])).resolve()
        domain = str(row["domain"]) if "domain" in row else "unknown_domain"
        model_name = str(row["model_name"]) if "model_name" in row else generated_py.stem

        # out_dir = wrapped_root / make_safe_filename(domain)
        # out_dir.mkdir(parents=True, exist_ok=True)

        # wrapped_file = out_dir / f"{make_safe_filename(model_name)}_wrapped.py"
        # existing_cellml = out_dir / f"{generated_py.stem}.cellml"

        domain_dir = wrapped_root / make_safe_filename(domain)
        model_dir = domain_dir / make_safe_filename(model_name)
        model_dir.mkdir(parents=True, exist_ok=True)

        wrapped_file = model_dir / f"{make_safe_filename(model_name)}_wrapped.py"
        existing_cellml = model_dir / f"{generated_py.stem}.cellml"
        existing_conditions_json = model_dir / f"{generated_py.stem}_conditions.json"

        if wrapped_file.exists() and not overwrite:
            success_rows.append(
                {
                    "model_name": model_name,
                    "domain": domain,
                    "generated_py_file": str(generated_py),
                    "wrapped_py_file": str(wrapped_file),
                    "copied_cellml_file": str(existing_cellml) if existing_cellml.exists() else "",
                    "conditions_json_file": str(existing_conditions_json) if existing_conditions_json.exists() else "",
                    "status": "skipped_exists",
                    "detail": "",
                }
            )
            print(f"[SKIP] {model_name} (already exists)")
            continue

        try:
            wrapped_py_file, copied_cellml_file, conditions_json_file = wrap_single_generated_file(
                generated_py_file=generated_py,
                wrapped_output_file=wrapped_file,
                model_name=model_name,
                copy_cellml=copy_cellml,
                write_conditions=write_conditions,
            )

            success_rows.append(
                {
                    "model_name": model_name,
                    "domain": domain,
                    "generated_py_file": str(generated_py),
                    "wrapped_py_file": str(wrapped_py_file),
                    "copied_cellml_file": str(copied_cellml_file) if copied_cellml_file else "",
                    "conditions_json_file": str(conditions_json_file) if conditions_json_file else "",
                    "status": "ok",
                    "detail": "",
                }
            )
            print(f"[OK] {model_name}")

        except Exception as e:
            failed_rows.append(
                {
                    "model_name": model_name,
                    "domain": domain,
                    "generated_py_file": str(generated_py),
                    "wrapped_py_file": str(wrapped_file),
                    "copied_cellml_file": "",
                    "conditions_json_file": "",
                    "status": "failed",
                    "detail": str(e),
                }
            )
            print(f"[FAIL] {model_name}: {e}")

    results_df = pd.DataFrame(success_rows + failed_rows)
    results_csv = wrapped_root / "batch_wrap_results.csv"
    results_df.to_csv(results_csv, index=False)

    print(f"\nProcessed: {len(success_rows) + len(failed_rows)}")
    print(f"Succeeded/skipped: {len(success_rows)}")
    print(f"Failed: {len(failed_rows)}")
    print(f"Summary written to: {results_csv}")

    return pd.DataFrame(success_rows), pd.DataFrame(failed_rows)


if __name__ == "__main__":
    summary_csv = "/Users/jasonz/Desktop/Honors Project/Physiome-ODE/cellml_export_summary.csv"
    wrapped_root = "/Users/jasonz/Desktop/Honors Project/Physiome-ODE/wrapped_models"

    success_df, failed_df = batch_wrap_from_summary(
        summary_csv=summary_csv,
        wrapped_root=wrapped_root,
        require_success_clean=True,
        skip_underconstrained=True,
        overwrite=True,
        copy_cellml=True,
        write_conditions=True,
    )

    print("\nDone.")