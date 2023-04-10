"""
EL COMERCIAL:
Eres un comercial trabajando para una compañía que vende diversos productos. 
Quieres crear un programa para realizar un seguimiento de los productos que has vendido y el valor total de las ventas. 
Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:

Producto 1: 3 unidades 
Producto 2: 1 unidad 
Producto 5: 7 unidades 
Producto 6: 2 unidades 
Producto 9 : 4 unidades

Los precios de cada uno de estos productos son como siguen:

Producto 1: 30.0 EU 
Producto 2: 9.8 EU 
Producto 3: 42.5 EU 
Producto 4: 32.6 EU 
Producto 5: 71.5 EU
Producto 6: 44.0 EU 
Producto 7: 21.2 EU 
Producto 8: 53.2 EU 
Producto 9: 25.3 EU 
Producto 10: 57.8 EU
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima la cantidad total de ventas, 
el dinero facturado por producto y el dinero total.

"""
#creamos una lista de listas donde tenemos el producto y el precio del producto
lista_producto = [[1, "Producto 1", 30], [2, "Producto 2", 9.8], [3, "Producto 3", 42.5], [4, "Producto 4", 32.6], [5, "Producto 5", 71.5], [6, "Producto 6", 44.0], [7, "Producto 7", 21.2], [8, "Producto 8", 53.2], [9, "Producto 9", 25.3], [10, "Producto 10", 57.8]]
lista_stock = [[1, "Producto 1", 10], [2, "Producto 2", 10], [3, "Producto 3", 10], [4, "Producto 4", 10], [5, "Producto 5", 10], [6, "Producto 6", 10], [7, "Producto 7", 10], [8, "Producto 8", 10], [9, "Producto 9", 10], [10, "Producto 10", 10]]

print("-----------------------")
print("Bienvenidos a este script que calculara el total de ventas, el dinero facturado por producto y el dinero total")
print("-----------------------")
print("Esta es la lista de Productos con sus correspondientes precios:")

#creamos una lista en 0 donde acumularemos los pedidos
lista_pedido = []

#imprimimos la lista
for i in range(0,10):
    print(i+1, ".", "El Artículo", lista_producto[i][1], "cuesta $", lista_producto[i][2])

print("-----------------------")

#creamos un bucle para que se ingresen todos los productos deseados
respuesta1 = True
respuesta2 = True
contador = 0

while respuesta1 == True:
    #pedimos por pantalla que ingrese el producto
    producto = input("Por favor ingrese el Artículo que desea comprar: ")
    cantidad = (input("Ingrese la cantidad de unidades de ese Artículo: "))
    #colocamos la comprobacion para que el programa verifique que estan ingresando los datos correctos
    if producto.isnumeric() == True and cantidad.isnumeric() == True:
        #comparamos el valor ingresado por pantalla con la lista
        for i in range(0,10):
            if int(producto) == lista_producto[i][0]:
                print("Usted eligió el Artículo ", lista_producto[i][1])
                #agregamos a la lista pedido la cantidad (como integer), el nombre del producto y el precio
                lista_pedido.append([int(cantidad), lista_producto[i][1], lista_producto[i][2]])
                pregunta = input("¿Desea comprar otro Articulo? s/n ")
                #creamos un bucle para que pregunte 
                respuesta2 = True
                while respuesta2 == True:
                    if pregunta == "s":
                        #nos aseguramos de finalizar este bucle pero que el primero no finalice y contamos los productos ingresados
                        respuesta2 = False
                        respuesta1 = True
                        contador += 1
                    elif pregunta == "n":
                        #nos aseguramos de que finalicen ambos bucles y contamos los productos ingresados
                        respuesta1 = False
                        respuesta2 = False
                        contador += 1
                    else:
                        #pedimos que ingresen nuevamente los "s" o "n"
                        pregunta = input("Debe ingresar 's' o 'n' ")
                        respuesta2 = True
    else:
        #si no se ingreso un numero de la lista de producto y una cantidad hay que intentarlo de nuevo
        print("Intentelo de nuevo. Debe ingresar una unica letra: ")
        #nos aseguramos que el segundo bucle se repita
        respuesta1 = True

#sumamos todo la facturacion total y la imprimimos
suma_total = 0
for i in range(0, contador):
    #multiplicamos la cantidad por el precio y lo sumamos
    suma_total = suma_total + (lista_pedido[i][0] * lista_pedido[i][2])

#calculamos la facturacion total por producto
print("-----------------------")
print("La facturacion por producto es:")
for i in range(0,contador):
    #imprimos el nombre del producto y la cantidad * por el precio
    print(lista_pedido[i][1], ":", lista_pedido[i][0]*lista_pedido[i][2])

#imprimimos la facturacion total
print("-----------------------")
print("La facturacion total es: ", suma_total)
