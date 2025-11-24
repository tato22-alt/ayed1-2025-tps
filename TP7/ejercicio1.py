def cantidad_digitos(n):
    """Esta función cuenta la cantidad de digitos de un número de manera recursiva 
    pre: recibe como parámetro un número entero
    post: retorna la cantidad de digitos que tiene este número"""
    try:
        if n < 0:
            n = abs(n)
        if n < 10:
            return 1
        else:
            return 1 + cantidad_digitos(n // 10)
    except TypeError:
        print("Error: Debe ingresar un número entero")
n = int(input("Ingrese un número para conocer la cantidad de digitos"))
cantidad = cantidad_digitos(n)

print(f"Cantidad de digitos en el número {n} son {cantidad}")