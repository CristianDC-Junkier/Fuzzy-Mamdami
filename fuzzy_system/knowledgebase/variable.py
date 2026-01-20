"""
variable.py
Define variables fuzzy y términos lingüísticos.
"""

from .membership import triangular


class FuzzyTerm:
    def __init__(self, name, mf_type, params):
        self.name = name
        self.mf_type = mf_type
        self.params = params

    def membership(self, x):
        if self.mf_type == "triangular":
            return triangular(x, *self.params)
        raise ValueError("Función no soportada")


class FuzzyVariable:
    def __init__(self, name, universe, terms):
        self.name = name
        self.universe = universe
        self.terms = terms
