def interrumpir_codigo(none = None)-> str:
    """pre: se carga una iteración con 10.000 números
    post: en caso de interrumpir el codigo, está contemplada una excepción"""
    try:
        for i in range(1,10001):
            print(i)
    except KeyboardInterrupt:
        print("Error: intentaste frenar el codigo")
        confirmacion = input("Presione ENTER para confirmar")
        if confirmacion == "":
            print("Saliendo...")
        else:
            print("Continuando...")
    

interrumpir_codigo()