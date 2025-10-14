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

def produccion_x_fabrica(produccion):
    total_x_fabrica = []

    for fabrica in (produccion):
        total = sum(fabrica)
        total_x_fabrica.append(total)

    return total_x_fabrica


def fabrica_mas_productiva(produccion):
    maximo = 0
    fila_max = 0
    col_max = 0

    for i, fila in enumerate(produccion):
        for j, cantidad in enumerate(fila):
            if cantidad > maximo:
                maximo = cantidad 
                fila_max = i                 
                col_max = j
    print(f"La mayor producción fue {maximo} bicicletas")
    print(f"En la fábrica {fila_max + 1}, el día {col_max + 1}")       


def menor_produccion_por_fabrica(produccion):
    menores = [(i, min(fabrica)) for i, fabrica in enumerate(produccion)]
    return menores

produccion = cargar_produccion(dias, fabricas)
print(produccion)
(fabrica_mas_productiva(produccion))
print(produccion_x_fabrica(produccion))
menor_produccion_por_fabrica(produccion)





