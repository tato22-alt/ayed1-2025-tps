numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
palos = ["oros", "copas", "bastos", "espadas"]


lista_cartas = [ f"{y} de {x}" for x in palos for y in  numeros]


print(lista_cartas)