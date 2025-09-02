def doble(x):
    return x * 2



def map_(doble,lista: list[int])-> list [int]:
    lista_interna = list()
    for elem in lista:
        lista_interna.append(doble(elem))
    return lista_interna

lista_original = [x for x in range(1,11)]

