def cargar_diccionario()-> dict[int]:
    """pre: Se crea un diccionario vacío
    post: En cada iteración se va cargando un número como clave y su valor es el cuadrado de ese número"""
    cuadrados = {}

    for n in range(21):
        cuadrados[n] = n*n
    print(cuadrados)


cargar_diccionario()