"""
Escribe un programa en Python para encontrar los elementos duplicados de una lista, 
añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los elementos únicos.
"""
#ejercicio 1
#defino 3 listas e imprimo la original
numeros = [1,2,3,4,5,6,3,7,8,9,8,10]
numeros_repetidos = []
numero_unicos = []
print("los numero originales son: ", numeros)

#para el primero for recorro la lista original y cuento los elementos que se repiten mas de una vez
for numero in numeros:
    if numeros.count(numero) > 1: 
        #si esos elementos no se encuentran en la lista repetidos los agrego a esa lista
        if numero not in numeros_repetidos:
           numeros_repetidos.append(numero)
    #de lo contrario los agrego a la lista de numeros unicos
    else:
        numero_unicos.append(numero)
#con un ultimo for recorro la lista de numeros repetidos y esos numeros los elimino de la numeros
for numero in numeros_repetidos:
    numeros.remove(numero)

"""
2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.
"""

#ejercicio 2
print("los numeros repetidos son: ", numeros_repetidos)
print("los numeros unicos son : ", numero_unicos)
print("la lista nueva es : ", numeros)

#unir 2 listas
lista_1 = [1,3,2,5,7,4,6,8,10,9]
lista_2 = [12,11,14,13,16,15,18,17,19,20]

#uso el comando extend para unir las listas y luego imprimo
lista_1.extend(lista_2)
lista_1.sort()
print(lista_1)

"""
3. Escribe un script que encuentre el segundo número más grande de una lista.
"""
#ejercicio 3
lista_3 = [1,2,3,4,5,6,3,7,8,9,8,10,2,300,12,20,35,54,222,104,32,655,43,123]
lista_3.sort()
#ordenamos la lista e imprimos el anteultimo numero (el segundo numero mas grande una lista)
print(lista_3)
print(lista_3[-2])

lista_3 = [1,2,3,4,5,6,3,7,8,9,8,10,2,300,12,20,35,54,222,104,32,655,43,123]
lista_3.sort(reverse=True)
#ordenamos la lista e imprimos el anteultimo numero (el segundo numero mas grande una lista)
print(lista_3)
print(lista_3[1])

"""
4. Crea un script que cuente el número de elementos más grandes que un determinado número
dado por el usuario (supón una lista numérica).
"""
#ejercicio 4
numero_usuario = (input("ingrese un numero: \n"))
lista_4 = [1,2,3,4,5,6,3,7,8,9,8,10,2,300,12,20,35,54,222,104,32,655,43,123]
lista_4.sort()
len_lista_4 = len(lista_4)
print(lista_4)

contador = 0
for i in range(0,len_lista_4):
    if int(numero_usuario) < lista_4[i]:
        contador += 1
print(contador)

"""
5. Crea un script dado un número introducido por el usuario o determinado al inicio del
programa, realice la suma de aquellos números que sean divisibles por este.
"""
#ejercicio 5
#creamos una lista
numero_usuario_5 = int(input("ingrese un numero para crear una lista de 1 hasta el numero: \n"))
lista_5 = list(range(1,numero_usuario_5+1))
print(lista_5)
numero_usuario_6 = int(input("ingrese un numero para ver la suma de los numeros divisibles por ese numero de la lista creada: \n"))

suma_total = 0

for i in range(0, numero_usuario_5-1):
    if lista_5[i] % numero_usuario_6 == 0:
        suma_total += lista_5[i]
print(suma_total)

"""
Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
que es inferior al número introducido o determinado al inicio del programa.
"""
#ejercicio 6
numero_usuario = (input("ingrese un numero: \n"))
lista_6 = [1,2,3,4,5,6,3,7,8,9,8,10,2,300,12,20,35,54,222,104,32,655,43,123]
lista_6.sort()
len_lista_6 = len(lista_6)

for num in lista_6:
    if numero_usuario > num:
        print(num)
        break
    
lista_6 = [1,2,3,4,5,6,3,7,8,9,8,10,2,300,12,20,35,54,222,104,32,655,43,123]
lista_6.sort()
print(lista_6)
len_lista_6 = len(lista_6)
numero_usuario = int(input("ingrese un numero: \n"))

for i in range(0, len_lista_6):
    if lista_6[i] < numero_usuario:
        resultado = lista_6[i]
print(resultado)

""" 
7. Crea un script que extraiga los elementos comunes entre dos listas.
"""

lista_7 = [3,5,6,7]
lista_8 = [1,2,3,4,5]
lista_9 = []

print(lista_7)
print(lista_8)
for num1 in lista_7:
    for num2 in lista_8:
        if num1 == num2:
            if num1 not in lista_9:
                lista_9.append(num1)
print(lista_9)

""" 
8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)

""" 

lista_10 = [1,2,3,4,5,2,1,2,3,1,2,1,4,5,56,1,2]
valor = int(input("ingrese un valor: "))

print(lista_10.count(valor))

"""
9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
números positivos de la lista original.
"""

lista_11 = [1,-2,1-3,5,-6,7,-9,10,-8,4]
lista_12 = []

for num in lista_11:
    if num > 0:
        lista_12.append(num)

print(lista_12)


"""
10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
los strings de la lista original.
"""

lista_13 = ["hola", "como", "estas", "todo", "bien"]
lista_14 = []

for word in lista_13:
    len_word = len(word)
    lista_14.append(len_word)

print(lista_14)

"""
11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
mayúscula.
"""
lista_15 = ["hola", "como", "estas", "todo", "bien"]
lista_16 = []

for word in lista_15:
    word_upper = word.upper()
    lista_16.append(word_upper)

print(lista_16)


