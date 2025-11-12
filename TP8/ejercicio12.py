productos = {
    "cuaderno tapa blanda": 3000,
    "lapiz": 1000,
    "lapicera": 1300,
    "cuaderno tapa dura": 3800,
    "tempera": 4700,
    "regla": 3200,
    "cuaderno a4": 5100
}

def actualizar_cuadernos(productos: dict[str, float]) -> dict[str, float]:
    """Aumenta un 15% solo a los productos que contienen la palabra 'cuaderno'.
    pre: Precios es un diccionario con nombres de productos como clave y precios numéricos como valor.
    post: Devuelve un nuevo diccionario con los cuadernos aumentados y el resto igual.
    """
    precio_nuevo = {}

    for producto, valor in productos.items():
        if "cuaderno" in producto.lower():
            precio_nuevo[producto] = round(valor * 1.15, 2)
        else:
            precio_nuevo[producto] = valor

    return precio_nuevo

def producto_mas_caro(precios: dict[str, float]) -> tuple[str, float]:
    """pre: Precios es un diccionario con nombres de productos como clave y precios numéricos como valor.
    post: Devuelve una tupla con el nombre del producto más caro y su precio.
    """
    mas_caro = max(precios, key=precios.get)
    return mas_caro, precios[mas_caro]

print("Lista de precios actualizada:", actualizar_cuadernos(productos))
print("El producto más caro es: ", producto_mas_caro(productos))