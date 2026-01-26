"""
defuzzifier.py
Defuzzificación usando PMV (Proportional Mean Value) desacoplado de la inferencia.
"""

def pmv_defuzz(output_var, activated_terms):
    """
    Calcula la salida crisp de una variable fuzzy usando PMV ponderado por la fuerza.

    Args:
        output_var: FuzzyVariable de salida con sus términos.
        activated_terms: Lista de tuplas [(fuerza, term_name), ...] calculadas en inferencia.

    Returns:
        Valor crisp de salida.
    """
    numerator = 0.0
    denominator = 0.0

    # Cada término contribuye proporcionalmente a su fuerza
    for strength, term_name in activated_terms:
        term = output_var.terms[term_name]
        center = term.params[1]  # Centro del triángulo

        numerator += center * strength
        denominator += strength

    # Evitar división por cero
    if denominator == 0:
        return 0.0

    return numerator / denominator
