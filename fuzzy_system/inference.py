"""
inference.py
Evalúa reglas fuzzy Mamdani con AND producto algebraico y Producto Lógico.
"""

def infer_rules(fuzzy_inputs, rules, output_var):
    """
    Evalúa la fuerza de activación de cada regla y aplica la implicación.

    Args:
        fuzzy_inputs: Diccionario con grados de pertenencia de cada variable de entrada.
        rules: Lista de reglas fuzzy.
        output_var: FuzzyVariable de salida (para aplicar implicación).

    Returns:
        rule_outputs: Lista de tuplas (fuerza de activación, term_name) lista para defuzzificación.
    """
    outputs = []

    for rule in rules:
        # Grados de pertenencia de los antecedentes
        strengths = [fuzzy_inputs[var][term] for var, term in rule.antecedent.items()]

        # AND = producto algebraico
        rule_strength = 1.0
        for s in strengths:
            rule_strength *= s

        # Producto Lógico (implicación) aplicado al consecuente
        # Cada término de salida recibe su fuerza multiplicada por la regla
        for var, term in rule.consequent.items():
            # Solo consideramos la variable de salida deseada
            if var == output_var.name:
                outputs.append((rule_strength, term))

    return outputs
