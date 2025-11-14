with open("nombres.txt", "r") as arch, \
     open("ARMENIA.TXT", "w") as arm, \
     open("ITALIA.TXT", "w") as ita, \
     open("ESPANIA.TXT", "w") as esp:

    for linea in arch:
        separar = linea.split(",")
        apellido = separar[0].strip()

        if apellido.endswith("ian"):
            arm.write(linea)
        elif apellido.endswith("ini"):
            ita.write(linea)
        elif apellido.endswith("ez"):
            esp.write(linea)
