cadena = "string"

def cadena_capicua(cadena: str)-> str:
    """pre: Recibe como parámetro una palabra y calcula si esta es capicúa o no
    post: Devuelve un mensaje en caso de que sea capicúa y otro mensaje en caso de que no lo sea """
    for i in range(len(cadena) // 2):
        if cadena[i] != cadena[-1 - i]:
            return print("No es capicúa")
    else:
        return print("Si, es capicúa")


assert cadena_capicua("neuquen") == True
assert cadena_capicua("hola") == False
assert cadena_capicua("oso") == True

(cadena_capicua(cadena))