def concatenar(a: int,b: int)-> int:
    """pre: Recibe dos números enteros
        post: Devuelve la concanteneción de una la suma de digitos de A y B"""
    aux = b
    dig = 0
    while aux > 0:
        aux = aux // 10
        dig += 1
    
    a = a *(10 ** dig)
    resultado = a + b
    return resultado

a = int(input("ingrese un numero A"))
b = int(input("ingrese un numero B"))

print(concatenar(a,b))