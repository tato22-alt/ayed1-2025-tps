ficha1 = (3,4)
ficha2 = (5,4)

def fichas_domino(ficha1: tuple, ficha2: tuple)-> bool:
    """Recibe dos fichas de dominó y devuelve True si pueden colocarse juntas.
    pre: Ficha1 y ficha2 son tuplas de 2 enteros.
    post: Devuelve True si comparten al menos un número, False en caso contrario."""
    return not set(ficha1).isdisjoint(ficha2)




print(fichas_domino(ficha1, ficha2))