from typing import List

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]

def intercalar_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    """pre: recibe dos listas de enteros, lista1 y lista2
    post: devuelve lista1 con los elementos de lista2 intercalados en posiciones calculadas"""
    for i, dato in enumerate(lista2):
        indice = i * 2 + 1
        lista1.insert(indice, dato)
    return lista1

resultado = intercalar_listas(lista1, lista2)
print(resultado)
