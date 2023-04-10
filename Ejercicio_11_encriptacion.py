"""
ENCRIPTACIÓN ROT13:
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.
[a,b,c,d,e,f,g,h,i,j,k,l,m] [H, O, L, A]
ROT13
[n,o,p,q,r,s,t,u,v,w,x,y,z] [U, B, Y, N]
1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
esta codificación ROT13 de la otra.
"""
#definimos el albabeto
abc = "abcdefghijklmnopqrstuvwxyz"

#pedimos que se ingrese una palabra
palabra = input("Ingrese una palabra: ")
palabra_encriptada = input("Ingrese otra palabra: ")

#seteamos en vacio la lista lista_rot_13
lista_rot_13 = []

#recorremos con un for la palabra ingresada
for i in range (0,len(palabra)):
    #recorremos con otro for el alfabeto
    for j in range(0, 25):
        #si j es menor que 13 y la letra de la palabra coincide con la del alfabeto
        if j < 13 and (palabra[i] == abc[j]):
            #entonces agrega la letra del alfabeto j+13 a la lista lista_rot_13
            lista_rot_13.append(abc[j+13])
        #si j es mayor que 13 y la letra de la palabra coincide con la del alfabeto
        elif j > 13 and (palabra[i] == abc[j]):
            #entonces agrega la letra del alfabeto
            lista_rot_13.append(abc[j-13])

#convertimos la lista a un string
palabra_rot = ''.join(lista_rot_13)
print(palabra_rot)

if palabra_encriptada == palabra_rot:
    print("Los mensajes", palabra, "y", palabra_encriptada, "son una encriptacion el uno del otro")
else:
    print("Los mensajes", palabra, "y", palabra_encriptada, "NO son una encriptacion el uno del otro")
