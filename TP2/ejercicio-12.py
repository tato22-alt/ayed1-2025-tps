from typing import List

def cargar_socios() -> List[int]:
    """pre: pide números de socio de 5 dígitos hasta ingresar 0
       post: devuelve la lista con todos los ingresos"""
    socios = []
    while True:
        num = int(input("Ingrese número de socio (5 dígitos, 0 para terminar): "))
        if num == 0:
            break
        if num < 10000 or num > 99999:
            print("Número inválido. Debe tener 5 dígitos.")
            continue
        socios.append(num)
    return socios

def informe_ingresos(socios: List[int]) -> None:
    """pre: recibe la lista de socios
       post: imprime cuántas veces ingresó cada socio"""
    socios_club = []
    for socio in socios:
        if socio not in socios_club:
            socios.append(socio)
            cantidad = socios.count(socio)
            print(f"el socio {socio} ingresó {cantidad} veces.")

def eliminar_socio(socios: List[int]) -> List[int]:
    """pre: recibe la lista de socios
       post: elimina todos los ingresos de un socio dado y muestra antes/después"""
    print("Registros antes de eliminar:", socios)
    baja = int(input("Ingrese el número de socio a dar de baja (5 dígitos): "))
    if baja < 10000 or baja > 99999:
        print("Número inválido. Debe tener 5 dígitos.")
    eliminados = socios.count(baja)
    socios = [s for s in socios if s != baja]
    print("Registros después de eliminar:", socios)
    print(f"Se eliminó {eliminados} ingresos del socio {baja}.")
    return socios


socios = cargar_socios()
print("Informe de ingresos")
informe_ingresos(socios)
socios = eliminar_socio(socios)
