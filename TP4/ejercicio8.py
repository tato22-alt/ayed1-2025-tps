def subcadena(cadena, n):
    """pre: recibe como parametro una cadena y la cantidad de caracteres que deben ser mostrados en pantalla
    post: devuelve la cantidad de caracteres solicitada, maneja excepciones"""
    largo = len(cadena)
    subcadena = {cadena[-n:]}
    try:
        if n > largo:
            raise ValueError
        print(f"Los últimos caracteres son {subcadena}")
    except TypeError:
        print("Error: ingresa un número entero")
        

cadena = input("Ingrese una frase/palabra")
n = int(input("Ingrese la cantidad de caracteres que desea ver: "))

subcadena(cadena, n)