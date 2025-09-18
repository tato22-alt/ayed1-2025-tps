encabezado = ["nombre", "legajo", "fecha"]

empleados = [
["juan perez", "12345", "15/03/1990"],
["Maria garcia", "54321", "10/11/1992"],
["carlos lopez","45345", "22/07/1976"],
["ana martines", "32454", "06/01/1988"],
["luis rodriguez", "12343", "05/02/1998"]
]

#a retornar
#salida = [
#[("nombre", "juan perez"), ("legajo", "12345"),("fecha","15/03/1990")]
#]

salida = []
for empleado in empleados:
    datos_empleado = []
    for par_de_datos in zip(encabezado, empleado):
        datos_empleado.append(par_de_datos)
    salida.append(datos_empleado)

#print(salida)

salida = [[par_de_datos for par_de_datos in zip(
encabezado,empleado)] for empleado in empleados if int(empleado[1]) > 20_000 and empleado[0][0] == "M"] 



print(datos_empleado)