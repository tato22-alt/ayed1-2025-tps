def es_triangular(num: int) -> str:
    """pre: recibe un número entero
        Post: devuelve un string informando si el número es triangular"""
    n = 1
    triangular = n * (n + 1) // 2
    while triangular <= num:
        if triangular == num:
            return "si, es triangular"
        n += 1
        triangular = n * (n + 1) // 2
    return "no es triangular"

def es_oblongo(num: int) -> str:
    """pre: recibe un número entero
        Post: devuelve un string informando si el número es oblongo"""
    n = 1
    oblongo = n * (n + 1)
    while oblongo <= num:
        if oblongo == num:
            return "si, es oblongo"
        n += 1
        oblongo = n * (n + 1)
    return "no es oblongo"


# Programa principal
numero = int(input("Ingrese un número a verificar: "))
print(f"¿Es triangular? {es_triangular(numero)}")
print(f"¿Es oblongo? {es_oblongo(numero)}")
