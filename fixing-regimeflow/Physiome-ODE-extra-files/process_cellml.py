import os
from typing import List, Dict, Any
import pandas as pd
from lxml import etree
from libcellml import Parser, Validator, Analyser, AnalyserVariable
from pathlib import Path

MATHML_NS = "http://www.w3.org/1998/Math/MathML"
NS = {"m": MATHML_NS}

# ----------------------------
# RAW MATHML COUNT
# ----------------------------
def count_equations_raw(cellml_text: str) -> Dict[str, Any]:
    try:
        root = etree.fromstring(cellml_text.encode("utf-8"))
    except Exception as e:
        return {
            "raw_error": str(e),
            "total_equations": None,
            "differential_equations": None,
            "algebraic_equations": None,
            "ode_like_equations": None,
            "pde_like_equations": None,
        }

    eq_nodes = root.xpath(".//m:apply[m:eq]", namespaces=NS)

    differential = 0
    algebraic = 0
    ode_like = 0
    pde_like = 0

    for eq in eq_nodes:
        has_diff = bool(eq.xpath(".//m:diff", namespaces=NS))
        has_partialdiff = bool(eq.xpath(".//m:partialdiff", namespaces=NS))

        if has_diff or has_partialdiff:
            differential += 1
            if has_partialdiff:
                pde_like += 1
            else:
                ode_like += 1
        else:
            algebraic += 1

    return {
        "raw_error": None,
        "total_equations": len(eq_nodes),
        "differential_equations": differential,
        "algebraic_equations": algebraic,
        "ode_like_equations": ode_like,
        "pde_like_equations": pde_like,
    }


# ----------------------------
# LIBCELLML ANALYSER COUNT
# ----------------------------
def count_with_libcellml(cellml_text: str) -> Dict[str, Any]:
    parser = Parser()
    model = parser.parseModel(cellml_text)

    parser_issues = [parser.issue(i).description() for i in range(parser.issueCount())]

    if model is None:
        return {
            "parsed": False,
            "state_count": None,
            "algebraic_count": None,
            "voi_count": None,
            "constant_count": None,
            "computed_constant_count": None,
            "parser_issues": parser_issues,
            "validation_issues": [],
            "analysis_issues": [],
        }

    validator = Validator()
    validator.validateModel(model)
    validation_issues = [validator.issue(i).description() for i in range(validator.issueCount())]

    analyser = Analyser()
    analyser.analyseModel(model)
    analysis_issues = [analyser.issue(i).description() for i in range(analyser.issueCount())]

    analysed_model = analyser.model()

    if analysed_model is None:
        return {
            "parsed": True,
            "state_count": None,
            "algebraic_count": None,
            "voi_count": None,
            "constant_count": None,
            "computed_constant_count": None,
            "parser_issues": parser_issues,
            "validation_issues": validation_issues,
            "analysis_issues": analysis_issues,
        }

    state_count = 0
    algebraic_count = 0
    voi_count = 0
    constant_count = 0
    computed_constant_count = 0

    for i in range(analysed_model.variableCount()):
        v = analysed_model.variable(i)
        t = v.type()

        if t == AnalyserVariable.Type.STATE:
            state_count += 1
        elif t == AnalyserVariable.Type.ALGEBRAIC:
            algebraic_count += 1
        elif t == AnalyserVariable.Type.VARIABLE_OF_INTEGRATION:
            voi_count += 1
        elif t == AnalyserVariable.Type.CONSTANT:
            constant_count += 1
        elif t == AnalyserVariable.Type.COMPUTED_CONSTANT:
            computed_constant_count += 1

    return {
        "parsed": True,
        "state_count": state_count,
        "algebraic_count": algebraic_count,
        "voi_count": voi_count,
        "constant_count": constant_count,
        "computed_constant_count": computed_constant_count,
        "parser_issues": parser_issues,
        "validation_issues": validation_issues,
        "analysis_issues": analysis_issues,
    }


# ----------------------------
# SINGLE FILE PROCESSOR
# ----------------------------
def process_cellml_file_equations(filepath: str) -> Dict[str, Any]:
    result = {
        "file": filepath,
        "file_name": os.path.basename(filepath),
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        result["read_error"] = str(e)
        return result

    raw = count_equations_raw(text)
    analysed = count_with_libcellml(text)

    warnings = []

    # Flag PDE-like content
    if raw.get("pde_like_equations", 0) and raw["pde_like_equations"] > 0:
        warnings.append("Contains <partialdiff/> (PDE-like)")

    # Flag mismatch
    if analysed.get("state_count") is not None:
        if raw.get("ode_like_equations") is not None:
            if analysed["state_count"] != raw["ode_like_equations"]:
                warnings.append("Mismatch: state_count vs raw ODE-like equations")

    # Flag issues
    if (
        analysed.get("parser_issues")
        or analysed.get("validation_issues")
        or analysed.get("analysis_issues")
    ):
        warnings.append("libCellML issues present")

    result.update({
        # RAW
        "total_equations": raw.get("total_equations"),
        "diff_eq_raw": raw.get("differential_equations"),
        "alg_eq_raw": raw.get("algebraic_equations"),
        "ode_like_raw": raw.get("ode_like_equations"),
        "pde_like_raw": raw.get("pde_like_equations"),

        # LIBCELLML
        "state_count": analysed.get("state_count"),
        "algebraic_count": analysed.get("algebraic_count"),

        # STATUS
        "warnings": "; ".join(warnings) if warnings else "",
        "has_issues": bool(warnings),
    })

    return result


# ----------------------------
# CORRECT VARIABLE COUNTING
# ----------------------------

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


def parse_cellml_file(cellml_path, strict_mode=False):
    text = Path(cellml_path).read_text(encoding="utf-8")
    parser = Parser(strict_mode)
    model = parser.parseModel(text)

    issues = []
    for i in range(parser.issueCount()):
        issues.append(parser.issue(i).description())

    return model, issues


def walk_components(component):
    """
    Recursively yield this component and all child components.
    """
    yield component
    for i in range(component.componentCount()):
        child = component.component(i)
        yield from walk_components(child)


def all_components(model):
    for i in range(model.componentCount()):
        comp = model.component(i)
        yield from walk_components(comp)


def variable_key(component, variable):
    return (component.name(), variable.name())


def collect_variables_and_equivalences(model):
    """
    Returns:
      all_vars: list of (component_name, variable_name)
      edges: list of ((component_name, variable_name), (component_name, variable_name))
    """
    all_vars = []
    edges = []

    # map Python object identity -> key
    var_obj_to_key = {}

    for comp in all_components(model):
        for j in range(comp.variableCount()):
            var = comp.variable(j)
            key = variable_key(comp, var)
            all_vars.append(key)
            var_obj_to_key[id(var)] = key

    # second pass: read equivalences
    for comp in all_components(model):
        for j in range(comp.variableCount()):
            var = comp.variable(j)
            k1 = variable_key(comp, var)

            for e in range(var.equivalentVariableCount()):
                eq_var = var.equivalentVariable(e)
                if eq_var is None:
                    continue

                #k2 = var_obj_to_key.get(id(eq_var))
                #if k2 is None:
                #    # fallback if object identity differs in your binding
                #    k2 = ("<unknown_component>", eq_var.name())

                eq_comp = eq_var.parent()
                if eq_comp is None:
                    # skip instead of inventing a fake component name
                    #continue
                    raise ValueError(f"Unable to find parent of {eq_var.name()}")

                k2 = (eq_comp.name(), eq_var.name())

                edges.append((k1, k2))

    return all_vars, edges


def build_variable_equivalence_classes(model):
    all_vars, edges = collect_variables_and_equivalences(model)

    uf = UnionFind()
    for v in all_vars:
        uf.add(v)

    for v1, v2 in edges:
        uf.add(v1)
        uf.add(v2)
        uf.union(v1, v2)

    groups = {}
    for v in uf.parent:
        root = uf.find(v)
        groups.setdefault(root, []).append(v)

    return {
        "all_variables": all_vars,
        "edges": edges,
        "groups": groups,
    }


def count_variables(model):
    result = build_variable_equivalence_classes(model)
    return {
        "raw_variable_count": len(result["all_variables"]),
        "unique_variable_count": len(result["groups"]),
        "equivalence_edge_count": len(result["edges"]),
        "equivalence_groups": result["groups"],
    }


def summarize_model_variables(cellml_path, strict_mode=False, show_groups=False):
    model, issues = parse_cellml_file(cellml_path, strict_mode=strict_mode)

    if model is None:
        raise ValueError("Failed to parse model.")

    counts = count_variables(model)

    print(f"File: {cellml_path}")
    print(f"Raw variables: {counts['raw_variable_count']}")
    print(f"Equivalence edges found: {counts['equivalence_edge_count']}")
    print(f"Unique variables after resolving equivalences: {counts['unique_variable_count']}")

    if issues:
        print("\nParser issues:")
        for issue in issues:
            print(f"  - {issue}")

    if show_groups:
        print("\nEquivalence groups:")
        for idx, members in enumerate(counts["equivalence_groups"].values(), start=1):
            print(f"  Group {idx}:")
            for comp_name, var_name in sorted(members):
                print(f"    {comp_name}.{var_name}")

    return counts


# ----------------------------
# SINGLE FILE PROCESSOR
# ----------------------------
def process_cellml_file(filepath: str) -> Dict[str, Any]:
    # equations
    equation_results = process_cellml_file_equations(filepath)
    model, _ = parse_cellml_file(filepath)
    variable_results = count_variables(model)
    return equation_results | variable_results
