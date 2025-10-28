import re

def validar_correo(correo):
    """Verifica si el correo cumple las reglas de formato."""
    patron = re.compile(r'^[A-Za-z0-9]+@[A-Za-z0-9.-]+\.(com|com\.ar)$', re.IGNORECASE)
    return patron.match(correo) 


def pedir_correos():
    """pre: Pide correos al usuario hasta que ingrese una cadena vacía.
       post: Devuelve un conjunto con los dominios válidos."""
    dominios = set()

    while True:
        correo = input("Ingrese un correo electrónico (Enter para finalizar): ").strip()
        if correo == "":
            break

        if validar_correo(correo):
            print("Correo válido.")
            dominio = correo.split("@")[1].lower()
            dominios.add(dominio)
        else:
            print("Correo inválido.")
    
    return dominios


def mostrar_dominios(dominios):
    """Muestra los dominios válidos ordenados alfabéticamente."""
    if not dominios:
        print("No se registraron dominios válidos.")
    else:
        print("Dominios válidos encontrados:")
        for dominio in sorted(dominios):
            print(dominio)

dominios_validos = pedir_correos()
mostrar_dominios(dominios_validos)