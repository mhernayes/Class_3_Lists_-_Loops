"""
ANALISIS DE VENTAS:
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los últimos 30 días. 
Quieres analizar las ventas por día de la semana para identificar los días de mayor venta.

Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo... 
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
Y otra lista con los días de la semana:
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“] 
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle p
ara añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la semana.

Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se 
reinicie a cero cuando llegue al séptimo día.
"""

#creamos la lista con las ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

suma_ventas = []

for i in range(0,30,7):
    for dias in dias_semana:
        if dias == "Lunes":
            suma_ventas.append(["Lunes", ventas[i]])

for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Martes":
            suma_ventas.append(["Martes", ventas[i]])

for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Miercoles":
            suma_ventas.append(["Miercoles", ventas[i]])

for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Jueves":
            suma_ventas.append(["Jueves", ventas[i]])

for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Viernes":
            suma_ventas.append(["Viernes", ventas[i]])
    
for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Sabado":
            suma_ventas.append(["Sabado", ventas[i]])

for i in range(1,30,7):
    for dias in dias_semana:
        if dias == "Domingo":
            suma_ventas.append(["Domingo", ventas[i]])

print(suma_ventas)

#creamos la lista con las ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

#creamos la lista con los dias de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#creamos la lista una lista vacia pero con las posiciones ya reservadas 
ventas_totales = [0,0,0,0,0,0,0]

#seteamos en 0 una variable que usremos para recorrer la lista ventas_totales
dia_venta = 0

#con un for recorremos la lista ventas
for venta in ventas:
    #si dia_venta es mayor que 6 quiere decir lo que se quiere guardar corresponde al dia domingo por lo que debemos
    #empezar a contar desde 0
    if dia_venta > 6: 
        dia_venta = 0
        #vamos guardando en la lista los valores de la lista ventas
        ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
        dia_venta = dia_venta + 1
    else:
        #cuanto no es domingo (dia_venta < 6), guardamos los valores en la lista ventas
        ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
        dia_venta = dia_venta + 1
    print(venta)

#imprimimos las ventas_totales  
dia = 0 

for vent in ventas_totales:
    print("La venta del dia", dias_semana[dia], "fue de:", vent)
    dia = dia + 1
    if dia == 7:
        dia = 0

#realizamos la suma
print("Las ventas totales son:")
print(sum(ventas_totales))