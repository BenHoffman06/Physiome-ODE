import ast
import re
from pathlib import Path


WRAPPER_MARKER = "# =========================\n# Auto-generated wrapper\n# =========================\n"


def sanitize_name(name: str) -> str:
    name = name.strip()
    name = name.split(" in component ")[0].strip()
    name = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    if not name:
        name = "unnamed"
    if name[0].isdigit():
        name = f"var_{name}"
    return name


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
    if hasattr(ast, "Index") and isinstance(sl, ast.Index):
        if isinstance(sl.value, ast.Constant) and isinstance(sl.value.value, int):
            return sl.value.value
    raise ValueError("Unsupported subscript index")


def extract_legend_names(text: str, array_name: str, size: int) -> dict[int, str]:
    pattern = re.compile(rf'{array_name}\[(\d+)\]\s*=\s*"([^"]+)"')
    names = {}
    for idx_s, raw in pattern.findall(text):
        idx = int(idx_s)
        if 0 <= idx < size:
            names[idx] = sanitize_name(raw)
    for i in range(size):
        names.setdefault(i, f"{array_name}_{i}")
    return names


def extract_init_consts_info(text: str):
    """
    Returns:
      direct_constants: {idx: rhs}
      derived_constants: {idx: rhs}
      state_assignments: {idx: rhs}
    """
    func_src = extract_function_source(text, "initConsts")
    tree = ast.parse(func_src)
    func = tree.body[0]

    direct_constants = {}
    derived_constants = {}
    state_assignments = {}

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
    out, cur, depth = [], [], 0
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
    return convert_custom_piecewise(expr)


def generate_parameters_block(size_constants, constant_names, direct_constants):
    lines = ["class Parameters:"]
    wrote_any = False
    for i in range(size_constants):
        if i in direct_constants:
            lines.append(f"    {constant_names[i]} = {direct_constants[i]}")
            wrote_any = True
    if not wrote_any:
        lines.append("    pass")
    return "\n".join(lines)


def generate_curve_names_block(state_names, algebraic_names):
    curve_names = [state_names[i] for i in sorted(state_names)] + [
        algebraic_names[i] for i in sorted(algebraic_names)
    ]
    lines = ["        self.curve_names = ["]
    for name in curve_names:
        lines.append(f'            "{name}",')
    lines.append("        ]")
    return "\n".join(lines)


def generate_y0_default_text(size_states, state_assignments):
    vals = [state_assignments.get(i, "0.0") for i in range(size_states)]
    return "[" + ", ".join(vals) + "]"


def generate_build_constants_block(size_constants, constant_names, direct_constants, derived_constants):
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

    lines.extend(["", "        return np.asarray(c, dtype=float)"])
    return "\n".join(lines)


def build_wrapper_text(text: str, model_name: str) -> str:
    size_states = extract_size(text, "sizeStates")
    size_algebraic = extract_size(text, "sizeAlgebraic")
    size_constants = extract_size(text, "sizeConstants")

    constant_names = extract_legend_names(text, "legend_constants", size_constants)
    state_names = extract_legend_names(text, "legend_states", size_states)
    algebraic_names = extract_legend_names(text, "legend_algebraic", size_algebraic)

    direct_constants, derived_constants, state_assignments = extract_init_consts_info(text)

    parameters_block = generate_parameters_block(
        size_constants, constant_names, direct_constants
    )
    curve_names_block = generate_curve_names_block(state_names, algebraic_names)
    y0_default = generate_y0_default_text(size_states, state_assignments)
    build_constants_block = generate_build_constants_block(
        size_constants, constant_names, direct_constants, derived_constants
    )

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
        self.model_name = "{model_name}"
{curve_names_block}
        self.params = param if param is not None else Parameters()
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
"""
    return wrapper.strip() + "\n"


def append_wrapper_to_file(input_path: str, output_path: str | None = None):
    in_path = Path(input_path)
    out_path = Path(output_path) if output_path else in_path.with_name(in_path.stem + "_wrapped.py")

    text = in_path.read_text(encoding="utf-8")
    if WRAPPER_MARKER in text:
        raise ValueError("Wrapper already appended.")

    wrapper = build_wrapper_text(text, model_name=in_path.stem)
    out_path.write_text(text.rstrip() + "\n\n\n" + wrapper, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    #out = append_wrapper_to_file("guyton_aldosterone_2008.py")
    out = append_wrapper_to_file("cartwright_husain_1986.py")
    print(f"Wrote: {out}")