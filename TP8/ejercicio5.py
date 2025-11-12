def ortogonales(v1: tuple, v2: tuple) -> bool:
    """Determina si dos vectores son ortogonales.
    Pre: v1 y v2 son tuplas de dos números que representan las componentes de cada vector.
    Post: Devuelve True si el producto escalar da 0, False si no.
    """
    x1, y1 = v1
    x2, y2 = v2
    producto = x1 * x2 + y1 * y2
    return producto == 0

assert ortogonales((2, 3), (-3, 2)) == True
assert ortogonales((1, 0), (0, 1)) == True
assert ortogonales((1, 1), (1, 0)) == False 