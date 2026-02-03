"""
main.py
Sistema fuzzy interactivo con validación por universo de discurso.
"""

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

# Variables de entrada definidas en tu sistema
input_vars = ["temperature", "humidity", "occupancy", "time_of_day"]

# Guardar rangos de universo de cada variable
var_ranges = {var: engine.input_vars[var].universe for var in input_vars}

while True:
    user_inputs = {}
    print("=== Sistema Fuzzy Interactivo ===")
    print("Ingresa los valores para las variables de entrada (o 'q' para salir).")
    
    # Pedir cada variable
    for var in input_vars:
        min_val, max_val = var_ranges[var]
        while True:
            val = input(f"{var} [{min_val}-{max_val}]: ")
            if val.lower() == 'q':
                print("Saliendo del sistema...")
                print("================================\n")
                exit(0)
            try:
                val = float(val)
                if val < min_val or val > max_val:
                    print(f"Valor fuera del rango permitido ({min_val} a {max_val}). Intenta de nuevo.")
                else:
                    user_inputs[var] = val
                    break
            except ValueError:
                print("Por favor ingresa un número válido o 'q' para salir.")
    
    # Ejecutar motor fuzzy
    fan_speed = engine.run(user_inputs, "fan_speed")
    print(f"Velocidad del ventilador: {fan_speed:.2f}%")
    print("================================\n")
