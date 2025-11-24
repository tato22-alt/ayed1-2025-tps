def producto(a, b):
    try:
        a = int(a)
        b = int(b)

        if b < 0:
            raise ValueError("El segundo número debe ser positivo")

        if b == 0:
            return 0
        else:
            return a + producto(a, b - 1)

    except ValueError:
        print("Error: debe ingresar números enteros y b ≥ 0.")

a = int(input("Ingrese un número entero A"))
b = int(input("Ingrese un número entero B"))

print("el producto de ambos números es", producto(a,b))