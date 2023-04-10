"""
LISTAS DE CARACTERES:
1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas de caracteres: 
manzana, plátano, cereza, pera, higo, frambuesa y fresa.
2. Usa la función len() para imprimir la longitud de la lista frutas.
3. Accede al objeto numero 3 de la lista e imprímelo or consola.
4. Modifica el segundo objeto de la lista y cambiado a mora.
5. Añade el string mango al final de la lista.
6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
llamada “ultima_fruta“.
9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
tengan más de 5 caracteres
12. Usa el método remove() para borrar el string “cereza“ de la lista.
13. Usa el método clear() para vaciar la lista.
"""

lista_frutas = ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]
print(len(lista_frutas))
print("\n")
print(lista_frutas[2])
lista_frutas[1] = "mora"
lista_frutas.append("mango")
lista_frutas.insert(0, "uva")
print(len(lista_frutas))
print("\n")
print(lista_frutas)
print("\n")
for i in range(0, len(lista_frutas)):
    print(lista_frutas[i])
ultima_fruta = lista_frutas.pop()
print("\n")
print(ultima_fruta)
for i in range(0, len(lista_frutas)):
    print(len(lista_frutas[i]))
print("\n")
for i in range(0, len(lista_frutas)):
    if (len(lista_frutas[i])) > 5:
        print(lista_frutas[i])
lista_frutas.remove("cereza")
print("\n")
print(lista_frutas)

lista_frutas.clear()
print(lista_frutas)