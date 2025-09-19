from typing import Tuple

def dia_de_la_semana(dia: int, mes: int, año: int) -> int:
    """
    pre: Recibe una fecha válida como día, mes y año
    post: Devuelve un número entero que representa el día de la semana
         
    """
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2

    siglo = año // 100
    año2 = año % 100

    diasem = ((26*mes - 2)//10 + dia + año2 + año2//4 + siglo//4 - 2*siglo) % 7
    if diasem < 0:
        diasem += 7
    return diasem

def pedir_mes_año() -> Tuple[int, int]:
    """
    pre: 
    post: Devuelve mes y año ingresados por el usuario, mes entre 1 y 12
    """
    while True:
        mes = int(input("Ingrese el mes (1-12): "))
        if 1 <= mes <= 12:
            break
        print("Mes inválido, debe estar entre 1 y 12.")
    
    año = int(input("In1grese el año: "))
    return mes, año

def dias_del_mes(mes: int, año: int) -> int:
    """
    pre: mes y año válidos
    post: devuelve la cantidad de días del mes considerando años bisiestos
    """
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29
    return dias_por_mes[mes - 1]

def imprimir_calendario(mes: int, año: int) -> None:
    """
    pre: mes y año válidos
    post: imprime el calendario del mes con semanas que empiezan en domingo
    """
    total_dias = dias_del_mes(mes, año)
    primer_dia_semana = dia_de_la_semana(1, mes, año)
    
    print("\nDom Lun Mar Mie Jue Vie Sab")
    print("    " * primer_dia_semana, end="")
    
    for dia in range(1, total_dias + 1):
        print(f"{dia:3}", end=" ")
        if (primer_dia_semana + dia) % 7 == 0:
            print()
    print()

mes, año = pedir_mes_año()
imprimir_calendario(mes, año)
