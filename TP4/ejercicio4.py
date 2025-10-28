
def validar_numero():
    """Pide un número entre 1 y 3999, validando el rango y el tipo de dato."""
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 3999: "))
            if 1 <= numero <= 3999:
                return numero 
            else:
                print("Por favor, ingrese un número dentro del rango 1 a 3999.")
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

def pasar_n_romanos(n: int)->str:
    numeros_romanos = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"}
    num = ""
    
    for valor, simbolo in numeros_romanos.items():
        cantidad = n // valor
        num += simbolo * cantidad
        n %=valor
    return num


numero_valido = validar_numero()
print("Número entero pasado a romano:", pasar_n_romanos(numero_valido))