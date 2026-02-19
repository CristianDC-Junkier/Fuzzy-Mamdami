"""
membership.py
Define funciones de pertenencia fuzzy.
"""

def triangular(x, a, b, c):
    """
    Función de pertenencia triangular corregida para extremos.
    """
    # Caso para el extremo de la derecha
    if b == c and x >= b:
        return 1.0
    
    # Caso para el extremo de la izquierda 
    if a == b and x <= b:
        return 1.0

    # Lógica estándar
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 1.0