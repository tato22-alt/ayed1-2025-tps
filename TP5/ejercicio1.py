def validar_num(none= None)-> int:
    """pre:se le pide al usuario un número natural (entero mayor que 0)
    post:valida el input usando excepciones. Devuelve el número válido
    """
    while True: 
        n = input("Ingrese un número entero positivo: ")  
        try:
            n = int(n) 
            if n <= 0: 
                print("Error: el número debe ser mayor que 0")
            else:
                print("Ingresaste correctamente el número:", n)
                return n  
        except ValueError: 
            print("Error: ingresaste un valor que no es un número entero")

validar_num()