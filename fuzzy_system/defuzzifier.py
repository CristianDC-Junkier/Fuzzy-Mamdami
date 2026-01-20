"""
defuzzifier.py
Desfuzzificación por centroide.
"""

import numpy as np


def centroid(output_var, rule_outputs, resolution=200):
    x_vals = np.linspace(*output_var.universe, resolution)
    aggregated = np.zeros_like(x_vals)

    for strength, consequent in rule_outputs:
        for _, term_name in consequent.items():
            term = output_var.terms[term_name]
            for i, x in enumerate(x_vals):
                aggregated[i] = max(
                    aggregated[i],
                    min(strength, term.membership(x))
                )

    if aggregated.sum() == 0:
        return 0.0

    return np.sum(x_vals * aggregated) / np.sum(aggregated)
