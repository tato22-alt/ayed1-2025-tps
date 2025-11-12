def tabla_de_multiplicar(n: int)-> str:
    """pre: Recibe un número entero y en base a eso crea un diccionario por comprensión con la tabla de multiplicación del N
    post: Retorna una tabla de multiplicación impresa centrada en pantalla"""
    tabla = {i: i * n for i in range(1,13)}
    for i, resultado in tabla.items():
        print(f"{n} x {i:2} = {resultado}")
    print("-" * 30)


n = int(input("Ingrese un número para generar una tabla de multiplicación"))

tabla_de_multiplicar(n)