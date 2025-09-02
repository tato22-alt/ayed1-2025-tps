def cargar_datos() -> None:
    """Pre: Pide tres números enteros al usuario.
    Post: llama a mayor_de_3 y muestra el resultado."""
    a = int(input("Ingrese un número a: "))
    b = int(input("Ingrese un número b: "))
    c = int(input("Ingrese un número c: "))
    print(mayor_de_3(a, b, c))

def mayor_de_3(a: int, b: int, c: int) -> str:
    """Pre: recibe como parámetros tres números enteros.
    Post: Devuelve el mayor, o -1 si el mayor se repite"""
    num = [a, b, c]
    num.sort()
    if num[2] > num[1]:
        return f"El mayor fue el número {num[2]}"
    elif num[2] == num[1]:
        return "-1"
    else:
        return "No existe un mayor estricto en esa secuencia de números"

cargar_datos()
