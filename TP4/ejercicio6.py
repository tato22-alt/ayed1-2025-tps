cadena = "El número de telefono es 2255-435414"

def extraer_subcadena(cadena,pos,cant):
    if pos > len(cadena) or cant > len(cadena):
        print("Algún dato es mayor al largo de la cadena")
    subcadena = cadena[pos : pos + cant]
    print(subcadena)


def extraer_subcadena_iterando(cadena,pos,cant):
    if pos > len(cadena) or cant > len(cadena):
        print("Algún dato es mayor al largo de la cadena")
    subcadena = ""
    for i in range(pos, pos + cant):
        subcadena += cadena[i]

try:
    pos = int(input("Ingrese la posición desde donde empieza la subcadena: "))
    cant = int(input("Ingrese la cantidad de caracteres a extraer: "))
    extraer_subcadena(cadena, pos, cant)
    extraer_subcadena_iterando(cadena,pos,cant)
except TypeError:
    print("Error: debe ingresar solo números.")

