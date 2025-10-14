import random as rn

def adivinar_numero():
    """pre: se carga un número aleatorio que el usuario deberá adivinar
      post: retorna la cantidad de intentos que se tardó en encontrar el número. En caso de no ingresar un digito está contemplado con una excepción"""
    para_adivinar = rn.randint(1,500)
    print(para_adivinar)
    intentos = 0
    n = 0
    try:
        while n != para_adivinar:
            n = int(input("Intente adivinar el número"))
            intentos += 1
            if n > para_adivinar:
                print("El número a adivinar es menor al ingresado")
            else:
                print("El número a adivinar es mayor al ingresado")

        print(f"Adivinaste, el número correcto es el {para_adivinar}. Lo lograste en {intentos} intentos")
    except ValueError:
        print("Error: Ingresaste algo que no es un dígito")
        intentos += 1

adivinar_numero()