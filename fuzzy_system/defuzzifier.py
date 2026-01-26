"""
defuzzifier.py
Defuzzificación usando PMV (Proportional Mean Value).
"""

def pmv_weighted(output_var, rule_outputs):
    """
    Calcula la salida numérica de una variable fuzzy utilizando PMV.
    Cada regla activada contribuye proporcionalmente a su fuerza sobre el centro del término.
    
    Usamos max por término en lugar de sumar todas las reglas porque:
    - Tenemos pocos términos de salida (low, medium, high) con centros separados.
    - Sumar todas las activaciones haría que el promedio salte a valores discretos (0/50/100).
    - Tomando el máximo por término, solo la regla más fuerte contribuye, dando resultados más estables.

    Args:
        output_var: Objeto FuzzyVariable de salida (ej. 'fan_speed') con sus términos.
        rule_outputs: Lista de tuplas (fuerza, consecuente) de cada regla activada.

    Returns:
        Valor real representando la salida defuzzificada.
    """

    # Si varias reglas activan el mismo término (por ejemplo 'high'), solo nos quedamos
    # con la que tiene mayor fuerza de activación. Esto evita que múltiples reglas 
    # similares influyan de manera excesiva en el resultado.
    max_activations = {}
    for strength, consequent in rule_outputs:
        for _, term_name in consequent.items():
            max_activations[term_name] = max(max_activations.get(term_name, 0.0), strength)

    # Inicializar acumuladores
    numerator = 0.0   # Acumula el total de (centro del término × fuerza)
    denominator = 0.0 # Acumula la suma de fuerzas para normalizar después

    # Calcular la contribución de cada término activado
    for term_name, strength in max_activations.items():
        if strength > 0:
            term = output_var.terms[term_name]
            center = term.params[1]  # Tomamos el pico del triángulo como valor representativo

            # Acumulamos para el promedio ponderado
            # Producto lógico implícito 
            # Cada regla activa contribuye proporcionalmente a su fuerza (matching)
            numerator += center * strength
            denominator += strength

    # Si ninguna regla se activó, devolvemos 0 para evitar dividir entre cero
    if denominator == 0:
        return 0.0

    # La salida final es el promedio ponderado de todos los centros activados
    return numerator / denominator
