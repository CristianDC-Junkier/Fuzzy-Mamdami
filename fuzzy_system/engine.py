"""
engine.py
Orquesta el sistema fuzzy completo.
"""

from fuzzy_system.knowledgebase import load_variables, load_rules
from fuzzy_system.fuzzifier import fuzzify
from fuzzy_system.inference import infer_rules
from fuzzy_system.defuzzifier import centroid


class MamdaniEngine:

    def __init__(self, variables_path, rules_path):
        self.input_vars, self.output_vars = load_variables(variables_path)
        self.rules = load_rules(rules_path)

    def run(self, inputs, output_name):
        fuzzy_inputs = fuzzify(inputs, self.input_vars)
        rule_outputs = infer_rules(fuzzy_inputs, self.rules)
        return centroid(self.output_vars[output_name], rule_outputs)
