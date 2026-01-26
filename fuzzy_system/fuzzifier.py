"""
fuzzifier.py
Convierte entradas crisp (valores numéricos concretos) a grados de pertenencia fuzzy.
"""

def fuzzify(inputs, input_vars):
    """
    Fuzzifica los valores de entrada.

    Args:
        inputs: Diccionario con valores numéricos concretos de las variables de entrada.
                Ejemplo: {'temperature': 32, 'humidity': 70, ...}
        input_vars: Diccionario de variables fuzzy (FuzzyVariable) que define los términos y 
                    sus funciones de membresía.

    Returns:
        fuzzy_inputs: Diccionario con los grados de pertenencia de cada término para cada variable.
                      Ejemplo: {'temperature': {'cold': 0.0, 'warm': 0.6, 'hot': 0.4}, ...}
    """

    fuzzy_inputs = {}  # Diccionario donde guardaremos los resultados de la fuzzificación

    # Recorremos todas las variables de entrada
    for var_name, value in inputs.items():
        variable = input_vars[var_name]  # Obtenemos la definición fuzzy de la variable

        # Calculamos el grado de pertenencia de cada término de la variable
        # term.membership(value) evalúa qué tanto pertenece 'value' a ese término
        fuzzy_inputs[var_name] = {
            term_name: term.membership(value)
            for term_name, term in variable.terms.items()
        }

    # Retornamos todos los grados de pertenencia
    return fuzzy_inputs
