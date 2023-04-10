"""
Crea un programa que imprima todos los números primos entre el 2 y el 100. 
Un numero primo es un numero positivo y entero mayor que uno que no tiene un 
divisor positivo y entero que no sea 1 o sí mismo.
"""
#vamos a resolver este ejercicio con 2 FOR
#con el primero recorremos los numeros del 2 al 100 (inclusive) para tomar ese numero(i) y dividirlo con el numero del segundo FOR (j)
for i in range(2,101):
    #para el numero del FOR (i) ese numero le asignamos valor TRUE
    primo = True
    #con el segundo FOR recorremos los numeros que se encuentran desde el 2 hasta numero elegido en el primer FOR (i). El numero i no esta incluido
    for j in range(2,i):
        #si el numero i lo dividimos por todos los numeros entre el 2 y el numero i (es ultimo no esta incluido) y el resto es 0, entonces no se trata de un numero primo.
        if i % j == 0:
            #si no se trata de un numero primo cambiamos la variable primo a FALSE
            primo = False
    #si la variable primo es TRUE imprimimos el valor i que será el numero primo
    if primo == True:
        #imprimimos todos los valores de i donde primo es TRUE. estos seran los numeros primos de acuerdo a la condicion del IF
        print(i)