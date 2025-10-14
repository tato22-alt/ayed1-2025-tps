import math

def calcular_raiz(none=None) -> str:
    """pre: se ingresa un número, debe ser entero positivo
    post: se calcula la raiz cuadrada de ese número y se muestra en pantalla"""
    try:
        n = int(input("Ingrese un número para calcular su raíz: "))
        if n < 0:
            print("Error: no se puede calcular la raíz de un número negativo")
        else:
            raiz = math.sqrt(n)
            print(f"La raíz del número {n} es igual a {raiz}")
    except ValueError:
        print("Error: no ingresaste un número entero")

calcular_raiz()
