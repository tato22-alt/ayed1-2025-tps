from typing import List

lista = [7,3,2]

def lista_ordenada(lista: List[int]) -> bool:
    """pre: recibe una lista de enteros
     post: compara indices para saber si es mayor el número que le sigue """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

print(lista_ordenada(lista))