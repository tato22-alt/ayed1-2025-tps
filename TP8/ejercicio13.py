edades = {
    "Pedro": 30,
    "Ana": 28,
    "Luis": 22,
    "Juan": 24,
    "Bautista": 22,
    "Jose": 27, 
    "Martin": 22
}

def buscar_clave(edades: dict, valor_buscado) -> list:
    """Pre: Edades es un diccionario con clave valor y valor_buscado es un valor posible dentro del diccionario.
    Post: Devuelve una lista con todas las claves cuyo valor coincide con valor_buscado."""
    claves = []

    for clave, valor in edades.items():
        if valor == valor_buscado:
            claves.append(clave)

    return claves

try:
    valor_buscado = int(input("Ingresá el valor que querés buscar en el diccionario: "))
    resultado = buscar_clave(edades, valor_buscado)
    print("Claves encontradas:", resultado)

except ValueError:
    print("Error: Debés ingresar un número entero.")