import random as rn
from typing import List

def matriz_sin_repetidos(n: int)-> List[List][int]:
    """pre: recibe un número entero equivalente al tamaño que tendrá la matriz al final
    post: retorna una matriz cargada con números enteros sin repetirse"""
    numeros = set()  
    while len(numeros) < n * n:
        num = rn.randint(0, n * n - 1)
        numeros.add(num)
    lista_n = list(numeros)
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(lista_n[i * n + j])
        matriz.append(fila)

    return matriz

n = int(input("Ingrese el tamaño de la matriz: "))

print(matriz_sin_repetidos(n))
