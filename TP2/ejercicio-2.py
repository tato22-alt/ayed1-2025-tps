import random as rn
from typing import List

def cargar_lista(tamaño: int) -> List[int]:
    """pre: recibe un número entero positivo
    post: devuelve una lista con enteros aleatorios entre 1 y 100
    """
    rn.seed(0)
    lista = []
    for _ in range(tamaño):
        lista.append(rn.randint(1, 100))
    return lista


def elementos_repetidos(lista: List[int]) -> List[int]:
    """pre: recibe una lista de enteros
    post: devuelve otra lista con los valores que aparecen más de una vez
    """
    repetidos = []
    for elemento in lista:
        if lista.count(elemento) > 1 and elemento not in repetidos:
            repetidos.append(elemento)
    return repetidos

tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = cargar_lista(tamaño)
print("Lista generada:", lista)

hay_repetidos = elementos_repetidos(lista)
if hay_repetidos:
    print("Elementos repetidos en la lista:", hay_repetidos)
else:
    print("No hay elementos repetidos en la lista.")
