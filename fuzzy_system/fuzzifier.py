"""
fuzzifier.py
Convierte entradas crisp a grados de pertenencia.
"""

def fuzzify(inputs, input_vars):
    """
    inputs: valores crisp
    input_vars: variables fuzzy

    return: grados de pertenencia
    """
    fuzzy_inputs = {}

    for var_name, value in inputs.items():
        variable = input_vars[var_name]
        fuzzy_inputs[var_name] = {
            term_name: term.membership(value)
            for term_name, term in variable.terms.items()
        }

    return fuzzy_inputs
