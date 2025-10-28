def centrar_texto(cadena: str)-> str:
    """pre: Recibe como parámetro una frase o palabra
    post: retorna el texto centrado en base a una disposición de 80 columnas"""
    centrar = (f"{cadena:^80}")
    return centrar

cadena = input("Ingrese una palabra/frase: ")

print(centrar_texto(cadena))
