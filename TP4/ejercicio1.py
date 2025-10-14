cadena = ["string"]

def cadena_capicua(cadena):
    for i in range (len(cadena)//2):
        if cadena[i] != cadena[-1-i]:
            print("no es capicua")
        else: 
            print("es capicua")
        

assert cadena_capicua("")