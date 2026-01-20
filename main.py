"""
main.py
Ejemplo del sistema fuzzy Mamdani.
"""

import os
import config
from fuzzy_system import MamdaniEngine

import os
from fuzzy_system import MamdaniEngine

# Rutas a los archivos JSON
variables_path = "data/variables.json"
rules_path = "data/rules.json"

# Comprobar que existen los archivos
if not os.path.isfile(variables_path):
    raise FileNotFoundError(f"No se encontró el archivo de variables: {variables_path}")
if not os.path.isfile(rules_path):
    raise FileNotFoundError(f"No se encontró el archivo de reglas: {rules_path}")

# Crear el motor Mamdani
engine = MamdaniEngine(variables_path, rules_path)


inputs = {
    "temperature": 32,
    "humidity": 70,
    "occupancy": 6,
    "time_of_day": 14
}

fan_speed = engine.run(inputs, "fan_speed")

print(f"Velocidad del ventilador: {fan_speed:.2f}%")
