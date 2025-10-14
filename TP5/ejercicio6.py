from typing import List
lista = []

def cargar_lista(lista: List[int])-> str:
    """pre: recibe una lista vacia
    post: se carga la lista mediante entradas del usuario y se busca el elemento solicitado mediante el metodo index"""
    while True:
        n = int(input("Ingrese un número entero para agregar a la lista: "))
        lista.append(n)
        if n == -1:
            break
    print(lista)
    elem = int(input("Ingrese un elemento a buscar en la lista y conocer su índice"))
    try:
        pos = lista.index(elem)
        print(f"El elemento {elem} se encuentra en la posición {pos}")
    except ValueError:
        print("Error: ese elemento no se encontró en la lista")


cargar_lista(lista)
