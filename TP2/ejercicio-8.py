from typing import List

def lista_impares(none) -> List[int]:
    """pre: recibe un parámetro cualquiera (no se utiliza)
    post: devuelve una lista con todos los números impares entre 101 y 200 inclusive"""
    impares = [n for n in range(101, 201, 2)]
    return impares

print(lista_impares(None))