from typing import List,Tuple

def cargar_pacientes() -> Tuple[List[int], List[int]]:
    """pre: carga pacientes
    post: devuelve dos listas"""
    urgencias = []
    turnos = []
    while True:
        afiliado = int(input("número de afiliado (4 dígitos, -1 para terminar):"))
        if afiliado == -1:
            break
        if afiliado < 1000 or afiliado > 9999:
            print("El número de afiliado debe tener 4 dígitos.")
            continue
        tipo = int(input("Ingrese 0 si es urgencia, 1 si es turno: "))
        if tipo == 0:
            urgencias.append(afiliado)
        elif tipo == 1:
            turnos.append(afiliado)
        else:
            print("Opción inválida, intente de nuevo.")
    return urgencias, turnos   

def contar_atenciones(urgencias: List[int], turnos: List[int]) -> None:
    """pre: recibe dos listas
    post: cuenta la cantidad de veces que aparece el número de afiliado en las listas y devuelve un mensaje"""
    while True:
        afiliado = int(input("Ingrese número de afiliado a buscar (-1 para terminar): "))
        if afiliado == -1:
            break
        cant_urgencias = urgencias.count(afiliado)
        cant_turnos = turnos.count(afiliado)
        print(f"Afiliado {afiliado}: {cant_urgencias} urgencias, {cant_turnos} turnos.")

urgencias, turnos = cargar_pacientes()
print("Urgencias:", urgencias)
print("Turnos:", turnos)
contar_atenciones(urgencias, turnos)