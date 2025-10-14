from typing import List

lista = [4, 3, 2, 7, 8, 22]

def porcentaje(lista: List[int]) -> List[float]:
    """pre: recibe una lista
    post: devuelve una lista indicando el porcentaje de cada elemento de la lista"""
    total = sum(lista)
    lista_nueva = []
    for elem in lista:
        lista_nueva.append(float(f"{elem / total:.2f}")) 
    return lista_nueva

print(porcentaje(lista))

