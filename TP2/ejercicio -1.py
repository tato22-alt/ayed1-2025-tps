import random as rn
from typing import List

def cargar_lista() -> List[int]:
    """pre: genera una lista de enteros aleatorios
       post: devuelve la lista cargada"""
    rn.seed(1)
    lista = []
    tamaño = rn.randint(10, 99)
    for _ in range(tamaño):
        lista.append(rn.randint(1000, 9999))
    return lista

def calcular_producto(lista: List[int]) -> int:
    """pre: recibe la lista cargada
       post: devuelve el producto de todos los elementos"""
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_n(lista: List[int]) -> List[int]:
    """pre: recibe una lista de enteros y pide un número al usuario
       post: elimina la primera aparición del número si está en la lista
             y devuelve la lista modificada. Si no está, avisa al usuario."""
    n = int(input("Ingrese el número a retirar de la lista: "))
    if n in lista:
        lista.remove(n)
        print(f"Se eliminó el número {n} de la lista.")
    else:
        print(f"El número {n} no está en la lista.")
    return lista

def es_capicua(lista: List[int]) -> None:
    """pre: recibe una lista de enteros
       post: imprime un mensaje diciendo si la lista es capicúa o no"""
    if lista == lista[::-1]:
        print("la lista es capicúa")
    else:
        print("la lista no es capicúa")

lista = cargar_lista()
producto = calcular_producto(lista)

print("Lista generada:", lista)
print(f"El producto de la lista es {producto}")
print("Lista luego de eliminar N", eliminar_n(lista))
print("¿Es capicúa?", es_capicua(lista))
