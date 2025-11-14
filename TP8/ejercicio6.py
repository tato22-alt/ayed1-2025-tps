def limpiar_frase() -> None:
    """pre: Se ingresa una frase por teclado
    post: Muestra las palabras sin repetir, ordenadas por longitud ignorando cualquier signo de puntuación"""
    try:
        frase = input("Ingresá una frase: ")

        if frase.strip() == "":
            raise ValueError("La frase no puede estar vacía.")

        limpia = ""
        for c in frase:
            if c.isalpha() or c.isspace():
                limpia += c

        palabras_unicas = set(limpia.split())
        ordenadas = sorted(palabras_unicas, key=len)

        print("Palabras ordenadas:", ordenadas)

    except ValueError as e:
        print("Error:", e)


limpiar_frase()