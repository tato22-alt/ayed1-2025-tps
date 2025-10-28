def filtrar_palabras(cadena, n):
    """pre: Recibe una frase y una cantidad de caracteres
    post: Retorna las palabras que tienen N o más letras"""
    filtrado = []                     
    juntar = cadena.split()          
    
    for palabra in juntar:            
        if len(palabra) >= n:         
            filtrado.append(palabra) 
    
    return " ".join(filtrado)         

def filtrar_x_comprension(cadena, n):
    juntar = cadena.split()
    filtrado = [palabra for palabra in juntar if len(palabra) >= n]
    return " ".join(filtrado)


def usando_filter(cadena, n):
    pass

cadena = input("Ingrese una frase: ")
n = int(input("Ingrese un número mínimo de letras: "))

print(filtrar_palabras(cadena, n))
print(filtrar_x_comprension(cadena,n))

