def dividir_archivo():
    """
    Divide un archivo de texto en partes sin cortar líneas.
    Cada parte tendrá como nombre parteN.txt
    """
    try:
        tam_max = int(input("Tamaño máximo por parte (en bytes): "))

        if tam_max <= 0:
            print("El tamaño debe ser mayor que cero.")
            return
        
        with open("texto.txt", "r") as arch:

            parte = 1
            tam_actual = 0
            salida = open(f"parte{parte}.txt", "w")

            for linea in arch:
                tam_linea = len(linea)

                
                if tam_actual + tam_linea > tam_max:
                    salida.close()
                    parte += 1
                    tam_actual = 0
                    salida = open(f"parte{parte}.txt", "w")

                salida.write(linea)
                tam_actual += tam_linea

            salida.close()
            print(f"Se generaron {parte} archivos.")

    except FileNotFoundError:
        print("No se encuentra el archivo.")

    except ValueError:
        print("Debe ingresar un número válido.")

    except Exception:
        print("Error inesperado al procesar el archivo.")

dividir_archivo()