from typing import List
def calcular_vuelto()-> str:
    """pre: La función recibe como parámetro una lista con las denominaciones de los billetes que hay
        post: Devuelve un mensaje con la cantidad de billetes de cada denominación necesario para dar el vuelto,
        en caso de que falte devolver menos de 10 pesos mostrará un mensaje
        La función calcula cuantos billetes debe entregar como vuelto"""
    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    vuelto = dinero_recibido - total_compra
    if vuelto < 0:
        print("el dinero recibido no es suficiente")
  
    if vuelto % 10 != 0:
        print(f"no es posible entregar el vuelto exacto, sobran {vuelto % 10} pesos")
    
    for b in denominaciones:
        cantidad = vuelto // b    
        if cantidad > 0:         
            print(f"{cantidad} billete(s) de ${b}")
        vuelto = vuelto % b    
        

calcular_vuelto()