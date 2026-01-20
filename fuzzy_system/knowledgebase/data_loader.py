"""
data_loader.py
Carga variables y reglas desde archivos JSON.
"""

import json
from .variable import FuzzyVariable, FuzzyTerm
from .rule import FuzzyRule

def load_variables(path):
    with open(path) as f:
        data = json.load(f)

    input_vars = {}
    output_vars = {}

    for name, v in data["input_variables"].items():
        input_vars[name] = _create_variable(name, v)

    for name, v in data["output_variables"].items():
        output_vars[name] = _create_variable(name, v)

    return input_vars, output_vars


def _create_variable(name, data):
    terms = {
        t: FuzzyTerm(t, d["type"], d["params"])
        for t, d in data["terms"].items()
    }
    return FuzzyVariable(name, data["universe"], terms)


def load_rules(path):
    with open(path) as f:
        rules_data = json.load(f)

    return [FuzzyRule(r["if"], r["then"]) for r in rules_data]
