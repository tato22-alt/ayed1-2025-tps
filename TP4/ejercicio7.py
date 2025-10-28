cadena = "El número de telefono es 2255-435414"

def eliminar_caracteres(cadena,pos,cant):
    if pos > len(cadena) or cant > len(cadena):
        print("Algún dato es mayor al largo de la cadena")
    subcadena = cadena[:pos] + cadena[pos + cant:]
    print(subcadena)

def eliminar_caracteres_iterando(cadena,pos,cant):
    subcadena = ""
    if pos > len(cadena) or cant > len(cadena):
        print("Algún dato es mayor al largo de la cadena")
    for i in range(len(cadena)):
        if i < pos or i >= pos + cant:
            subcadena += cadena[i]
    print(subcadena)

try:
    pos = int(input("Ingrese la posición desde donde empieza la subcadena: "))
    cant = int(input("Ingrese la cantidad de caracteres a extraer: "))
    eliminar_caracteres(cadena, pos, cant)
except TypeError:
    print("Error: debe ingresar solo números.")