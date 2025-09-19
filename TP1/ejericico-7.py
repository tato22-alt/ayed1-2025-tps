from typing import Tuple

def es_bisiesto(año: int) -> bool:
    """pre: recibe un año
       post: devuelve True si el año es bisiesto, False en caso contrario"""
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_mes(mes: int, año: int) -> int:
    """pre: recibe mes y año
       post: devuelve la cantidad de días del mes considerando si es bisiesto"""
    if mes == 2:
        if es_bisiesto(año):
            return 29
        return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def pedir_fecha_valida() -> Tuple[int, int, int]:
    """pre: -
       post: solicita día, mes y año por teclado hasta que se ingrese una fecha válida
             y devuelve la fecha como (dia, mes, año)"""
    while True:
        dia = int(input("Ingrese día: "))
        mes = int(input("Ingrese mes: "))
        año = int(input("Ingrese año: "))
        
        if 1 <= mes <= 12 and 1 <= dia <= dias_mes(mes, año):
            return dia, mes, año
        print("Fecha inválida, ingrese nuevamente.")

def dia_siguiente(dia: int, mes: int, año: int) -> Tuple[int, int, int]:
    """pre: recibe día, mes y año válidos
       post: devuelve la fecha del día siguiente como (dia, mes, año)"""
    if dia < dias_mes(mes, año):
        dia += 1
    else:
        dia = 1
        if mes < 12:
            mes += 1
        else:
            mes = 1
            año += 1
    return dia, mes, año


fecha = pedir_fecha_valida() 
fecha_siguiente = dia_siguiente(*fecha)  
print(f"El día siguiente a {fecha[0]}/{fecha[1]}/{fecha[2]} es {fecha_siguiente[0]}/{fecha_siguiente[1]}/{fecha_siguiente[2]}")
