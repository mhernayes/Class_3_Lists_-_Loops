"""
SCRABBLE:
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de Scrabble. 
Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el segundo el numero
que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la ficha con la letra A 
y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos en una mano de scrabble. 
El valor total será la suma de los puntos de todas las fichas de la mano.
"""
#definomos la lista de letras y puntos
lista = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5], ["f", 6], ["g", 6], ["h", 7], ["i", 8], ["j", 9], ["k", 10], ["l", 11], ["m", 12], ["n", 13], ["ñ", 14], ["o", 15], ["p", 16], ["q", 17], ["r", 18], ["s", 19], ["t", 20], ["u", 21], ["v", 22], ["w", 23], ["x", 24], ["y", 25], ["z", 26]]
#seteamos vacia la lista mano
mano = []

mensaje = """------------- Bienvenidos al Scrable -------------
El programa le solicitará que ingrese su mano. 
Debe ingresar una letra a la vez.
La mano es de máximo 8 letras.

"""

#pedimos que ingrese la mano
#seteamos en 0 el contador y la variable respuesta que repetira el bucle
cant = 0
#letra mano debe empezar en uno para que el for vaya de 0 a 2
letra_mano = 1

respuesta1 = True
respuesta2 = True
#colocamos un bucle para limitar el numero de respuestas.
while cant < 8:
        #usamos un for para recorrer la mano
        #pedimos la letra, la agregamos a la lista mano y preguntamos si quire continuar
        while respuesta1 == True:
            letra = str(input("ingrese una unica letra: "))
            if letra.isalpha() == True and len(letra) == 1:
                mano.append(letra)
                pregunta = input("Desea ingresar otra letra? s/n: ")
                #seteamos las dos respuestas como True para los 2 while.
                respuesta1 = True
                respuesta2 = True
                while respuesta2 == True:
                    if pregunta == "s":
                        #la variable cant es para el bucle y la variable letra_mano es para saber realmente cuantas manos tiene
                        cant += 1
                        letra_mano += 1
                        #seteamos respuesta2 = False para finalizar el bucle
                        respuesta2 = False
                    elif pregunta == "n":
                        #finalizamos los 2 bucles
                        respuesta2 = False
                        respuesta1 = False
                        cant = 9
                    else: 
                        pregunta = input("Debe ingresar 's' o 'n': ")
                        #nos aseguramos que el ultimo bucle se repita
                        respuesta2 = True
            else:
                print("Intentelo de nuevo. Debe ingresar una unica letra: ")
                #nos aseguramos que el segundo bucle se repita

#imprimos el resultado de la mano              
print("su mano es: " , mano)

#con 2 for recorremos la lista "lista" y la lista "letra_mano"
resultado = 0
for i in range(0,27):
    for j in range(0,letra_mano):
        #cuando se cumpla la condicion, se iran sumando los puntos
        if mano[j] == lista[i][0]:
            resultado = resultado +lista[i][1]
print("Usted sumara " , resultado, " puntos")

"""
#con 2 for recorremos la lista "lista" y la lista "letra_mano"
resultado = 0
for i in lista:
    for j in mano:
        #cuando se cumpla la condicion, se iran sumando los puntos
        if j == lista[i][0]:
            resultado = resultado + lista[i][1]
print("Usted sumara " , resultado, " puntos")
"""