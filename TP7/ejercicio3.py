def suma_recursiva(n):
    """Esta función suma de manera recursiva un número
    pre: recibe un número entero
    post: retorna la suma de los números hasta llegar al número que se pasa como parámetro """    
    try:
        if n == 1:
            return 1
        else:
            return n + suma_recursiva(n - 1)
    except TypeError:
        print("Error: Debe ingresar un número entero")

n = 22
resultado = suma_recursiva(n)
print(f"La suma de los números del 1 al {n} es: {resultado}")