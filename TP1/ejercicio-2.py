from typing import List

def fecha_valida(dia: int, mes: int, año: int) -> bool:
    """pre: Recibe una lista y valida los datos ingresados esten en el rango de los meses del año y los días del mes
     post:En base a los datos recibidos devuelve si el año es bisiesto o no"""
    dias_por_mes: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes < 1 or mes > 12:
        return False

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

assert fecha_valida(29, 2, 2024) == True
assert fecha_valida(29, 2, 2023) == False
assert fecha_valida(31, 4, 2022) == False
assert fecha_valida(31, 12, 2022) == True
assert fecha_valida(0, 5, 2022) == False
assert fecha_valida(15, 13, 2022) == False

print(fecha_valida(29, 2, 2024))   
print(fecha_valida(29, 2, 2023))  
print(fecha_valida(31, 4, 2022))   
print(fecha_valida(31, 12, 2022)) 
print(fecha_valida(0, 5, 2022))    
print(fecha_valida(15, 13, 2022)) 
