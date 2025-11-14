def cargar_diccionario()-> dict[int]:
    """pre: Se crea un diccionario vacío
    post: En cada iteración se va cargando un número como clave y su valor es el cuadrado de ese número"""
    try:
        cuadrados = {}

        for n in range(21):
            cuadrados[n] = n*n
        print(cuadrados)
        
    except Exception:
        print("Ocurrió un error al cargar el diccionario")

cargar_diccionario()