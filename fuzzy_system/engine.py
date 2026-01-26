"""
engine.py
Orquesta el sistema fuzzy completo.
"""

from fuzzy_system.knowledgebase import load_variables, load_rules
from fuzzy_system.fuzzifier import fuzzify
from fuzzy_system.inference import infer_rules
from fuzzy_system.defuzzifier import pmv_defuzz  # Ahora renombrado para ser genérico

class MamdaniEngine:
    """
    Motor fuzzy Mamdani que ejecuta todo el flujo:
    Fuzzificación -> Inferencia -> Defuzzificación
    """

    def __init__(self, variables_path, rules_path):
        # Cargar variables de entrada/salida y reglas desde JSON
        self.input_vars, self.output_vars = load_variables(variables_path)
        self.rules = load_rules(rules_path)

    def run(self, inputs, output_name):
        """
        Ejecuta el motor fuzzy completo para una variable de salida.

        Args:
            inputs: Diccionario de valores crisp de las entradas.
            output_name: Nombre de la variable de salida (ej. 'fan_speed').

        Returns:
            Valor crisp defuzzificado de la salida.
        """
        # Fuzzificar las entradas
        fuzzy_inputs = fuzzify(inputs, self.input_vars)

        # Inferir la fuerza de activación de cada regla
        rule_outputs = infer_rules(fuzzy_inputs, self.rules, self.output_vars[output_name])

        # Defuzzificar usando PMV
        return pmv_defuzz(self.output_vars[output_name], rule_outputs)
