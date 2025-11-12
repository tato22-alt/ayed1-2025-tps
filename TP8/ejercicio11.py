def contarvocales(cadena: str) -> dict[str, int]:
    """pre: Recorre cada letra de la frase o palabra
    post: Acumula la cantidad de vocales en un diccionario"""
    vocales = "AEIOUaeiou"
    contador = {}

    for letra in cadena:
        if letra in vocales:
            letra = letra.lower()
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    return contador

cadena = input("Ingrese una palabra o frase: ")

print(contarvocales(cadena))