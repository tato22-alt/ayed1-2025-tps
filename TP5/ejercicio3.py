def reconocer_mes(none = None)-> str:
    """pre: se carga una lista con los meses del año
    post: devuelve el número correspondiente al mes, en caso de error están contempladas dos excepciones"""
    meses = ["enero", "febrero", "marzo","abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    mes = int(input("Ingrese el número de mes, recibirá su nombre: "))
    try:
        print(f"El mes que corresponde a ese número es el mes {meses[mes - 1]}")
    except IndexError:
        print("Error: ingresaste un mes no válido")
    except TypeError:
        print("Error: no ingresaste un número")


reconocer_mes()