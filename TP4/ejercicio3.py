def separar_claves(clave_maestra: int)-> str:
    """pre: recibe un número entero 
    post: usando rebanadas separa la clave en números dos grupos: pares e impares"""
    cadena = str(clave_maestra)
    clave1 = cadena[0::2] 
    clave2 = cadena[1::2] 
    return clave1, clave2

clave_maestra = int(input("Ingrese la clave"))

print(separar_claves(clave_maestra)) 