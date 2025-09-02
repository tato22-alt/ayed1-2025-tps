def gasto_mensual_subte(cant_viajes: int)-> str:
    """pre: Recibe una lista con la cantidad de viajes realizados en un mes
        post: Dependiendo de la cantidad de viajes realizados le aplica un descuento a partir de los 20 viajes
        la funciión sirve para calcular descuentos en lso viajes realizados durante un mes en subterraneo"""
    valor_boleto = 1032

    if cant_viajes >= 1 and cant_viajes <= 20:
        descuento = 1
    elif cant_viajes >= 21 and cant_viajes <= 30:
        descuento = 0.80
    elif cant_viajes >= 31 and cant_viajes <= 40:
        descuento = 0.70
    elif cant_viajes >= 41 and cant_viajes <= 200:#aclaro un rango limitado teniendo en cuenta que 200 viajes tal vez sean muchos
        descuento = 0.60
    else:
        return "la cantidad ingresada no es válida"
    total = cant_viajes * valor_boleto * descuento
    return f"el total fue de ${total}"

cant_viajes = int(input("ingrese la cantidad de viajes que realizó en el mes"))

print(gasto_mensual_subte(cant_viajes))

