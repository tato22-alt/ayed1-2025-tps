a = "222"
b = "778"

def convertir_a_entero(a,b: str)-> int:
    """pre: recibe dos cadenas de caracteres
    post: devuelve la suma de estos dos digitos o en caso de no poder realizar la suma retorna -1"""
    try:
        a = int(a)
        b = int(b)
        suma = a + b
    except ValueError:
        print("-1")
    else: 
        print(suma)
    
    

(convertir_a_entero(a,b))

    
