from typing import List

def cuadrado_lista() -> List[int]:
    """pre: recibe un entero N ingresado por teclado
       post: devuelve una lista con los cuadrados de los números de 1 a N
             y solo imprime los últimos 10 valores"""
    n = int(input("Ingrese N: "))
    cuadrados = []
    i = 1
    while i <= n:
        cuadrados.append(i*i)
        i += 1
    
    ultimos_10 = cuadrados[-10:] 
    print(f"Los últimos 10 números cuadrados son: {ultimos_10}")
    return ultimos_10


cuadrado_lista()
