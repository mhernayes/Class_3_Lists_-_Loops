"""
NUMEROS PRIMOS 2:
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva 
lista con los números primos de la lista original. 
Además, el script debe devolver el número total de números primos encontrados y la suma 
de los números primos encontrados

"""
#creamos una lista de enteros
lista = list(range(2,101))
lista_primos = []
for numero in lista:
    primo = True
    for n in range(2, numero):
        if numero % n == 0:
            primo = False
    if primo == True:
        print(numero)
        lista_primos.append(numero)

print(lista_primos)

print(sum(lista_primos))
print(len(lista_primos))
