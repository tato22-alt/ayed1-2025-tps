import random as rn
from typing import List, Tuple

def generar_pesos(cantidad: int) -> List[int]:
    """pre: recibe la cantidad de naranjas cosechadas
       post: devuelve una lista con pesos simulados de cada naranja (150-350 g)"""
    return [rn.randint(150, 350) for _ in range(cantidad)]

def verificar_pesos(pesos: List[int]) -> Tuple[List[int], int]:
    """pre: recibe una lista de pesos de naranjas
       post: devuelve dos valores:
            lista de naranjas válidas (200 a 300 g)
            cantidad de naranjas para jugo (fuera de rango)"""
    naranjas_validas = []
    jugo = 0
    for peso in pesos:
        if 200 <= peso <= 300:
            naranjas_validas.append(peso)
        else:
            jugo += 1
    return naranjas_validas, jugo

def contar_cajones(naranjas_validas: List[int]) -> Tuple[int, int]:
    """pre: recibe lista de naranjas válidas
       post: devuelve:
        cantidad de cajones completos (100 naranjas por cajón)
        sobrante de naranjas para el siguiente reparto"""
    cajones = len(naranjas_validas) // 100
    sobrante = len(naranjas_validas) % 100
    return cajones, sobrante

def calcular_camiones(naranjas_validas: List[int]) -> int:
    """pre: recibe lista de naranjas válidas
       post: devuelve la cantidad de camiones necesarios para transportar la cosecha
             considerando que cada camión soporta 500 kg y no se despacha si ocupa < 80%"""
    peso_total_kg = sum(naranjas_validas) / 1000  
    camiones = int(peso_total_kg // 500)
    if (peso_total_kg % 500) / 500 >= 0.8:
        camiones += 1
    return camiones

cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))
pesos = generar_pesos(cantidad)
naranjas_validas, jugo = verificar_pesos(pesos)
cajones, sobrante = contar_cajones(naranjas_validas)
camiones = calcular_camiones(naranjas_validas)

print(f"Naranjas válidas: {len(naranjas_validas)}")
print(f"Naranjas para jugo: {jugo}")
print(f"Cajones completos: {cajones}")
print(f"Sobrante de naranjas: {sobrante}")
print(f"Camiones necesarios: {camiones}")
