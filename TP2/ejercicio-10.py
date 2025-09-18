from typing import List
import random as rn

def cargar_lista() -> List[int]:
    """pre: genera una lista de enteros aleatorios
       post: devuelve la lista cargada"""
    rn.seed(1)
    lista = []
    tamaño = rn.randint(10, 99)
    for _ in range(tamaño):
        lista.append(rn.randint(100, 999))
    return lista

def es_impar(n: int) -> bool:
    """pre: recibe un número entero
       post: devuelve True si el número es impar"""
    return n % 2 != 0

def filtrar_impares(lista: List[int]) -> List[int]:
    """pre: recibe una lista de enteros
       post: devuelve una nueva lista con los valores impares"""
    return list(filter(es_impar, lista))


lista = cargar_lista()
impares = filtrar_impares(lista)

print("Lista original:", lista)
print("Lista de impares:", impares)
