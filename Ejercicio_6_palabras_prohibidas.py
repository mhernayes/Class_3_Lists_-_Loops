"""
PALABRAS PROHIBIDAS:
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna letra prohibida.
"""

#crear lista aleatoria de 5 palabras
lista_palabras = []

for i in range(0,5):
    palabra = input("ingrese una la palabra: ")
    lista_palabras.append(palabra)

print("La lista de palabras aleatorias es: ", lista_palabras)

#crear lista de palabras que contenga 3 letras
lista_letras = []
for i in range(0,3):
    letra = input("ingrese una letra: ")
    lista_letras.append(letra)

print("La lista de letras aleatorias es: ", lista_letras)

#crear lista de palabras que no contengan las letras prohibidas

lista_filtrada = []
for palabra in lista_palabras:
    if lista_letras[0] not in palabra and lista_letras[1] not in palabra and lista_letras[2] not in palabra:
        lista_filtrada.append(palabra)
    
print("La lista filtrada es: ", lista_filtrada)

