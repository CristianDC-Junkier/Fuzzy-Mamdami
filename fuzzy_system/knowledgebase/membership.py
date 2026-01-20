"""
membership.py
Define funciones de pertenencia fuzzy.
"""

def triangular(x, a, b, c):
    """
    Función de pertenencia triangular.
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 1.0
