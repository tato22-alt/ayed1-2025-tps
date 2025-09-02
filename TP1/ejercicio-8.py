import random as rn

def generar_pesos(cantidad: int)-> list[int]:
    """pre: recibe la cantidad de naranjas
        post: genera una lista de pesos"""
    pesos = []
    for i in range(cantidad):
        peso = rn.randint(100,400)
        pesos.append(peso)
    return pesos

def verificar_pesos():
    pesos = generar_pesos()
    cajon = 0
    jugo = 0
    for naranjas in pesos:
        if naranjas >= 200 and naranjas <= 300:
            cajon += 1
        else:
            jugo += 1
    return cajon, jugo

def contar_cajones():
    pass
