"""
inference.py
Evalúa reglas fuzzy Mamdani.
"""

def infer_rules(fuzzy_inputs, rules):
    """
    Aplica AND = MIN
    """
    outputs = []

    for rule in rules:
        strengths = [
            fuzzy_inputs[var][term]
            for var, term in rule.antecedent.items()
        ]
        outputs.append((min(strengths), rule.consequent))

    return outputs
