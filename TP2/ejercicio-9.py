from typing import List

def lista_multiplos() -> List[int]:
    """pre: solicita al usuario los valores A y B
    post: devuelve una lista con los múltiplos de 7 entre A y B que no sean múltiplos de 5"""
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    lista = [num for num in range(a, b + 1) if num % 7 == 0 and num % 5 != 0]
    return lista


resultado = lista_multiplos()
print("Múltiplos de 7 que no son múltiplos de 5 entre A y B:")
print(resultado)
