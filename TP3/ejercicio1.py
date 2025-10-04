from typing import List

matriz = []

def cargar_matriz(matriz: List[List][int])-> List[List][int]:
    """pre: recibe una lista vacia
    post: devuelve una lista de listas cargada con numeros ingresados por el usuario"""
    n = int(input("Ingrese N: "))
    for f in range(n):
        fila = []
        for c in range(n):
            valor = int(input(f"Ingrese un numero para la posición {f}, {c}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def ordenar_matriz(matriz):
    for fila in matriz:
        fila.sorted()  
    return matriz


def cambiar_filas(matriz: List[List][int])-> List[List][int]:
    """pre: recibe una matriz (lista de listas) y le pide al usuario dos filas a cambiar
    post: devuelve la matriz con las filas intercambiadas"""
    fila_1 = int(input("Ingrese la primera fila a intercambiar: "))
    fila_2 = int(input("Ingrese la segunda fila a intercambiar: "))
    
    if fila_1 < 0 or fila_1 >= len(matriz):
        print("La fila", fila_1, "no existe en la matriz")
        return matriz

    if fila_2 < 0 or fila_2 >= len(matriz):
        print("La fila", fila_2, "no existe en la matriz")
        return matriz
    
    matriz[fila_1], matriz[fila_2] = matriz[fila_2], matriz[fila_1]
    return matriz


def cambiar_columnas(matriz: List[List][int])-> List [int]:
    """pre: recibe una matriz de números enteros
    post: intercambia las columnas luego de validar que estas columnas estén dentro de la matriz"""
    col_1 = int(input("Ingrese la primera columna a intercambiar: "))
    col_2 = int(input("Ingrese la segunda columna a intercambiar: "))
    
    while col_1 < 0 or col_1 >= len(matriz):
        print("La columna", col_1, "no existe en la matriz")
        col_1 = int(input("Ingrese la primera columna a intercambiar: "))

    while col_2 < 0 or col_2 >= len(matriz):
        print("La columna", col_2, "no existe en la matriz")
        col_2 = int(input("Ingrese la segunda columna a intercambiar: "))
    
    for fila in matriz:
        fila[col_1], fila[col_2] = fila[col_2], fila[col_1]
    return matriz

def transponer_matriz(matriz: List[List][int])->List[List][int]:
    """pre: recibe una matriz cargada con números enteros
    post: intercambia el número de la posición de la fila y lo coloca en la posición de la columna"""
    n = len(matriz)
    for f in range (n):
        for c in range(f+1, n):
            matriz[f][c], matriz[c][f] = matriz[c][f], matriz[f][c]
    return matriz

def promedio_matriz(matriz: List[List][int])-> str:
    """pre: recibe una fila de la matriz cargada con números enteros
    post: calcula el promedio de la fila y retorna el valor esperado """
    fila = int(input("ingrese el número de fila para informar su promedio"))
    while fila < 0 or fila >= len(matriz):
        print("la fila no pertenece a la matriz")
        fila = int(input("ingrese el número de fila para informar su promedio"))
    suma_fila = sum(matriz[fila])
    promedio_fila = suma_fila / len(matriz[fila])
    print(f"el promedio de la fila es {promedio_fila}")

def porcentaje_impares(matriz: List[List][int])-> str:
    """pre: recibe una columna de la matriz cargada con números enteros 
    post: suma la cantidad de números impares incluidos en esa columna y calcula el porcentaje de números impares """
    impares = 0
    columna = int(input("ingrese la columna a verificar"))
    for fila in matriz:
        if matriz[columna] % 2 != 0:
            impares += 1
    porcentaje = (impares / len(matriz[columna])) * 100
    return f"el porcentaje de impares en la columna fue {porcentaje}"

def simetrica_principal(matriz: List[List][int])-> str:
    """pre: recibe una matriz cargada con números enteros
     post: compara cada elemento de la matriz para comprobar si la diagonal principal es simetrica o no lo es"""
    n = len(matriz)  
    for i in range(n):
        for j in range(i + 1, n): 
            if matriz[i][j] != matriz[j][i]: 
                return "diagonal asimétrica"
    return "diagonal simétrica"

def simetrica_secundaria(matriz: List[List][int])-> str:
    """pre: recibe una matriz cargada con números enteros
     post: compara cada elemento de la matriz para comprobar si la diagonal secundaria es simetrica o no lo es"""
    n = len(matriz)  
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return "diagonal asimétrica"
    return "diagonal simétrica"


print("Matriz cargada:")
print(cargar_matriz(matriz))

print("Matriz ordenada:")
print(ordenar_matriz(matriz))

print("Matriz con filas intercambiadas:")
print(cambiar_filas(matriz))

print("Matriz con columnas intercambiadas:")
print(cambiar_columnas(matriz))

print("Matriz transpuesta(intercambiar filas por columnas)")
print(transponer_matriz(matriz))

print(promedio_matriz(matriz))
print(porcentaje_impares(matriz))

print(simetrica_principal)

print(simetrica_secundaria)