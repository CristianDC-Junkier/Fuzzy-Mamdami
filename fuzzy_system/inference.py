"""
inference.py
Evalúa reglas fuzzy Mamdani.
"""

def infer_rules(fuzzy_inputs, rules):
    """
    Evalúa la fuerza de activación de cada regla fuzzy Mamdani.

    Args:
        fuzzy_inputs: Diccionario con grados de pertenencia de cada variable de entrada.
                      Ejemplo: {'temperature': {'cold':0.7,'warm':0.3,...}, ...}
        rules: Lista de reglas fuzzy, cada una con:
               - antecedent: dict de condiciones de entrada {'temperature':'cold', ...}
               - consequent: dict de salida {'fan_speed':'medium'}

    Returns:
        Lista de tuplas: [(fuerza_de_activacion, consecuente), ...]
    """

    outputs = []  # Lista donde guardaremos la fuerza de cada regla y su consecuente

    # Recorremos todas las reglas
    for rule in rules:
        # Obtenemos la fuerza de cada antecedente en la regla
        # fuzzy_inputs[var][term] devuelve el grado de pertenencia del valor de entrada
        strengths = [
            fuzzy_inputs[var][term]
            for var, term in rule.antecedent.items()
        ]

        # AND como producto algebraico
        # Calcula la fuerza total de la regla combinando todos los antecedentes
        rule_strength = 1.0
        for s in strengths:
            rule_strength *= s  # producto de todos los grados de pertenencia

        # Guardamos la fuerza de activación y el consecuente
        outputs.append((rule_strength, rule.consequent))

    # Retornamos todas las reglas con su fuerza de activación
    return outputs
