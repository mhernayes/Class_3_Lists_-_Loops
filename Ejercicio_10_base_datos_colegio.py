"""
BASE DE DATOS DE UN COLEGIO:
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los estudiantes de un clase. 
En tu base de datos tienes una lista con los nombres de los estudiantes y para cada estudiante debes guardar sus notas 
provenientes de deberes, exámenes y proyectos. También necesitas calcular a nota media de cada estudiante y la nota 
media de la clase al completo.

Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para cada estudiante. 
Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota media de cada estudiante. 
También puedes usar otro bucle para calcular la nota media de toda la clase.
"""
#definimos la lista de alumnos
lista_alumnos = [[1, "Juan Perez"], [2, "Jorge Gomez"], [3, "Pablo Martinez"]]
promedio_total = 0

def notas(lista_alumnos):
    
    lista_notas = []  

    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #con un for recorremos la lista lista_alumnos y vamos ingresando las notas 
            for i in range(0, len(lista_alumnos)):
                print("Ingrese los notas del siguiente alumno: ", lista_alumnos[i][1])
                #ingresa por pantalla el numero de la nota
                nota_deberes = int(input("Por favor ingrese la Nota Deberes del alumno: "))
                nota_tp = int(input("Por favor ingrese la Nota Trabajo Practico del alumno: "))
                nota_examen = int(input("Por favor ingrese la Nota Examen del alumno: "))
                lista_notas.append([lista_alumnos[i][1], nota_deberes, nota_tp, nota_examen])    
        #se controla los datos ingresados con un try except
        except ValueError:
            print("Los datos ingresados no son correctos")       
        break            
    #la variable que se devuelve es lista_notas
    return lista_notas
#mensaje
print("-----------------------")
print("Bienvenidos a la Escuela de Conquer")

#imprimos la lista de estudiantes
print("-----------------------")
print("Esta es la lista de Estudiantes:")
for i in range(0,3):
    print(lista_alumnos[i][0], ".", lista_alumnos[i][1])

print("\n")
print("-----------------------")
#imprimos la lista de notas
print("Las notas que ingresara, seran las siguientes:")
print("1. Nota Deberes")
print("1. Nota Trabajos Practicos")
print("1. Nota Examenes")

#se llama a la funcion y se imprime la lista_notas
lista_notas = notas(lista_alumnos)
""" 
#la variable prom que devuelve la funcion prom es igual a resultado_notas
resultado_notas = prom(lista_notas, lista_alumnos)
"""
#imprimos las notas por alumno y calculamos el promedio del alumno
for i in range(0, len(lista_notas)):
    print("El alumno ", lista_notas[i][0], "tiene las siguientes notas: ")
    print("Nota Deberes: ", lista_notas[i][1])
    print("Nota Trabajos Practicos: ", lista_notas[i][2])
    print("Nota Examen: ", lista_notas[i][3])
    promedio_alumno = (lista_notas[i][1] + lista_notas[i][2] + lista_notas[i][3]) / 3
    print("Su promedio de Notas es: ", promedio_alumno)
    print()
    #acumulamos el total de todas las notas en la variable promedio_total
    promedio_total = promedio_total + promedio_alumno

#calculamos el promedio total
promedio_total = promedio_total / len(lista_alumnos)

print("El promedio total de todas las notas de todos los alumnos es: ", promedio_total)



