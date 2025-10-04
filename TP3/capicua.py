lista = [2,4,3,4,2]

for i in range (len(lista)//2):
    if lista[i] != lista[-1-i]:
        print("no es capicua")
    else: print("es capicua")