"""
LISTAS NUMERICAS:
1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
consola.
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
compresión).
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
6. Haz lo mismo con el número más alto
7. Suma todos los elementos de la lista con y sin un bucle.
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
el punto 2.
"""

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_numeros_pares = []
lista_numeros_pares_inversos = []

for i in range(0, len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        print(lista_numeros[i])
        lista_numeros_pares.append(lista_numeros[i])

print("\n")
for j in range(len(lista_numeros_pares)-1, -1, -1):
    lista_numeros_pares_inversos.append(lista_numeros_pares[j])

for k in range(0, len(lista_numeros_pares_inversos)):
    print(lista_numeros_pares_inversos[k])


print("\n")
for i in range(0, len(lista_numeros)):
    print(lista_numeros[i]** 2)

print("\n") 
print(min(lista_numeros))
print(max(lista_numeros))
print(sum(lista_numeros))

print("\n") 
for l in range(0, len(lista_numeros_pares_inversos)):
    if lista_numeros_pares_inversos[l] == 8:
        print(l)
