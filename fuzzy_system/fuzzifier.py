"""
fuzzifier.py
Convierte entradas crisp a grados de pertenencia fuzzy.
"""

def fuzzify(inputs, input_vars):
    """
    Calcula el grado de pertenencia de cada entrada a sus términos fuzzy.

    Args:
        inputs: Diccionario con valores crisp de entrada.
        input_vars: Diccionario de FuzzyVariable con términos y funciones de membresía.

    Returns:
        fuzzy_inputs: Diccionario con los grados de pertenencia de cada término.
    """
    fuzzy_inputs = {}

    # Recorremos cada variable de entrada
    for var_name, value in inputs.items():
        variable = input_vars[var_name]

        # Evaluamos la membresía de cada término para el valor de entrada
        fuzzy_inputs[var_name] = {
            term_name: term.membership(value)
            for term_name, term in variable.terms.items()
        }

    return fuzzy_inputs
