import random as rn

def cargar_lista():
    rn.seed(0)
    lista = []
    tamaño = rn.randint(10, 99)   
    for _ in range(tamaño):       
        lista.append(rn.randint(1000, 9999)) 
    return lista

lista = cargar_lista()
print(lista)
print("Tamaño de la lista:", len(lista))
