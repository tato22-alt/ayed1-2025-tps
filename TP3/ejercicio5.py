import random as rn
from typing import List

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]

fabricas = int(input("Ingrese la cantidad de fábricas: "))

def cargar_produccion(dias: List[str], fabricas: int)-> List[int]:
    produccion_semanal = []  
    for f in range(fabricas): 
        fabrica = []
        for d in range(len(dias)): 
            cantidad = rn.randint(0,150) 
            fabrica.append(cantidad)     
        produccion_semanal.append(fabrica) 
    return produccion_semanal


produccion = cargar_produccion(dias, fabricas)

print(produccion)

def produccion_x_fabrica(fabricas, dias):
    for i in fabricas:
        print(i)

print(produccion_x_fabrica(fabricas,dias))
