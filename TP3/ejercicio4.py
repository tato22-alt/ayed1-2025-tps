import random as rn
from typing import List

def cargar_asientos(none)-> List[List][int]:
    """pre: pide al usuario que cargue la cantidad de filas y columnas que tendrá la sala de cine
    post: retorna una matriz cargada con la cantidad de asientos de la sala de cine"""
    sala_cine = []
    filas = int(input("ingrese la cantidad de filas: "))
    butacas = int(input("ingrese la cantidad de butacas por fila: "))

    for f in range(filas):
        fila = []
        for b in range(butacas):
            estado = rn.randint(0, 1)  
            fila.append(estado)       
        sala_cine.append(fila)       
    return sala_cine

sala = cargar_asientos()
  
def mostrar_butacas(sala: List[List][int])-> str:
    """pre: recibe una matriz cargada con números enteros
    post: imprime en pantalla como estan ubicados los asientos de la sala"""
    print("estado de la sala: ")
    for fila in sala:
        print(fila)

mostrar_butacas(sala)

def reservar(sala: List[List][int])-> bool:
    """pre: recibe una matriz cargada de números enteros
    post: retorna True en caso de que se pueda reservar la butaca o False en caso de que no sea posible reservar"""
    fila = int(input("ingrese una fila para modificar la butaca"))
    butaca = int(input("ingrese la butaca a reservar"))
    while fila < 0 or fila >= len(sala):
        print("fila inexistente")
        fila = int(input("ingrese una fila para modificar la butaca"))
    while butaca < 0 or butaca >= len(sala[fila]):
        butaca = int(input("ingrese la butaca a reservar"))
    if sala[fila -1][butaca -1] == 0:
        sala[fila -1][butaca -1] = 1
        for fila in sala:
            print(fila)
        return True
    else: 
        return False

def butacas_libres(sala: List[List][int])-> str:
    """pre: recibe una matriz cargada con números enteros
    post: retorna la cantidad de butacas libres dentro de la sala"""
    libres = 0
    for fila in sala:
        for butaca in fila:
            if butaca == 0:
                libres += 1

    return f"hay {libres} butacas disponibles"

print(reservar(sala))
print(butacas_libres(sala))