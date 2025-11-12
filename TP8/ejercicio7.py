numeros = {0,1,2,3,4,5,6,7,8,9}

def eliminar_n(numeros):
    """Elimina números de un conjunto de a uno, maneja excepciones en caso de que no es
    pre: Recibe un conjunto de números enteros seguún el número que elija el usuario 
    post: Imprime en pantalla los números restantes"""
    while True:
        print(numeros)
        a_eliminar = input("Ingrese un número del 0 al 9 para eliminarlo del conjunto")
        
        try:
            num = int(a_eliminar)
        except ValueError:
            print("Debe ingresar un número")
            continue
        if num == -1:
            break
        else:
            try:
                numeros.remove(num)
            except KeyError:
                print("Ese número no se encuentra en el conjunto")
eliminar_n(numeros)