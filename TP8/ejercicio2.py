def fecha_extendida()-> str:
    """pre: Solicita al usuario una fecha separada por espacios con el mes en números
    post: Convierte ese número al mes correspondiente y se imprime en pantalla """
    try:
        entrada = input("Ingrese día, mes y año separados por espacio: ")
        partes = entrada.split()  

        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])

        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

        
        if 1 <= mes <= 12:
            print(dia, "de", meses[mes-1], "de", anio)
        else:
            print("El mes ingresado no es válido. Debe estar entre 1 y 12.")

    except ValueError:
        print("Error: ingresá solo números separados por espacios.")
    except IndexError:
        print("Error: asegurate de escribir día, mes y año.")

fecha_extendida()