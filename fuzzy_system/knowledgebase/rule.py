"""
rule.py
Define reglas fuzzy Mamdani.
"""

class FuzzyRule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
