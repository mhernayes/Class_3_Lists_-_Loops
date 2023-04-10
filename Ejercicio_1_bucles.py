""""
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una estructura como la de más abajo, 
donde el valor de entrada es el número de estrellas en el centro de la estructura.
*
** 
***
**** 
***** 
**** 
*** 
**
*
"""

#solicitar un numero por pantalla
numero = int(input("Ingrese un numero:\n"))
print("---------------")
for i in range(0, numero):
    asterisco = "*" * i
    print(asterisco)
for i in range(numero, 0, -1):
    asterisco = "*" * i
    print(asterisco)


"""
2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

ingresar = False
while ingresar == False:
    contraseña = input("Por favor ingrese la contraseña: \n")
    if contraseña == "casa":
        print("Contraseña correcta, puede ingresar.")
        ingresar = True
    elif contraseña != "casa":
        print("Contraseña incorrecta.")

"""
3. Crea un script que pida al usuario una palabra y luego muestre por pantalla 
una a una las letras de la palabra introducida empezando por la última.
"""

palabra = input("ingrese una palabra:\n")
len_1 = int(len(palabra))
for i in range((len_1-1), -1, -1):
    print(palabra[i])

"""
 Crea un programa en el que se pregunte al usuario por una frase y una letra, 
 y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
cantidad = 0
palabra_2 = input("ingrese una palabra:\n")
letra = input("ingrese una letra:\n")
len_2 = int(len(palabra_2))
for i in range(0, len_2):
    if letra == palabra_2[i]:
        cantidad += 1
print("La letra " , letra, " se repite: ", cantidad, " veces")
