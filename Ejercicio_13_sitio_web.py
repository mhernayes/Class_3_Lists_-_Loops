""" VALIDAR ACCESO A UN SITIO WEB:
Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios a un sitio web. 
Crea un script que verifique si el nombre de usuario y la contraseña ingresados son correctos y permita el 
acceso solo si ambos son correctos.
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo... nombres_usuario = ["juan123", "ana456", „pedro789"]
Y otra lista con las contraseñas guardadas para cada usuario...
contraseñas = ["clave123", "clave456", „clave789"]
Otra opción puede ser que crees una lista de listas con la forma: nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["pedro789“, "clave789“] ]
Despues puedes pedir el usuario y contraseña y comprobar si coinciden.
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde recorras los nombres de usuario 
y compruebes con un if si el nombre de usuario introducido y la contraseña coinciden con los datos de tus listas.

"""
#utilizamos 2 listas, una de nombres donde buscaremos el usuario y la otra donde buscaremos la clave correcta
lista_nombres= ["juan123", "ana456", "pedro789"]
lista_contraseñas = [["juan123", "clave123"], ["ana456", "clave456"], ["pedro789", "clave789"]]

print("---------------------")

#definimos la funcion fun_nombre que es para ingresar el nombre correcto.
def fun_nombre(lista_nombres):
    #seteamos los intentos en 3 y el nombre_corecto en vacio
    intentos = 3
    nombre_correcto = ""
    #el while repetira siempre que intentos sea mayor que 0 
    while intentos > 0:
        #pedimos que se ingrese el nombre de usuario
        print("Por favor, ingrese su nombre de usuario. Intentos restantes:", intentos)
        nombre_usuario = input()
        #si el nombre de usuario esta en lista_nombres el nombre ingresado es correcto, llevamos a 0 los intentos para finalizar el bucle
        if nombre_usuario in lista_nombres:
            print("El nombre ingresado es correcto")
            #cuando se encuentra el nombre se guarda en nombre_correcto
            nombre_correcto = nombre_usuario
            intentos = 0
        #si no se encuentra el nombre se imprime el mensaje nombre incorrecto y se descuenta en 1 los intentos
        elif nombre_usuario not in lista_nombres:
            print("El nombre es incorrecto")
            intentos = intentos - 1
    #la variable que se devuevle es nombre_correcto
    return(nombre_correcto)


def fun_contraseña(nombre_correcto, lista_contraseña):
    intentos = 3
    #seteamos la variable contraseña_correcta en vacio
    contraseña_correcta = ""
    #si nombre_correcto es vacio no pide contraseña
    if nombre_correcto != "":
        #el while repetira siempre que intentos sea mayor que 0 
        while intentos > 0:
            #pedimos que se ingrese la contraseña para el nombre de usuario ingresado
            print("Por favor, ingrese la contraseña de:", nombre_correcto, ". Intentos restante:", intentos)
            contraseña = input()
            #con un for recorremos la lista contraseña desde 0 hasta la longitud de la lista
            for i in range(0, len(lista_contraseña)):
                #verificamos si el nombre_correcto y la contraseña coinciden con los datos de lista
                if nombre_correcto == lista_contraseña[i][0] and contraseña == lista_contraseña[i][1]:
                    #si coinciden gurdamos la contraseña en la variable contraseña_correcta y llevamos a 0 la variable intentos para finalizar el while
                    contraseña_correcta = contraseña
                    print("Contraseña correcta")
                    intentos = 0
                #verficamos si la variable nombre_correcto esta en la lista pero no coincide la contraseña restamos en 1 1 los intentos
                elif nombre_correcto == lista_contraseña[i][0] and contraseña != lista_contraseña[i][1]:
                    print("Clave incorrecta")
                    contraseña_correcta = "Contraseña Incorrecta"
                    intentos = intentos - 1  
    #devolvemos la variable contraseña_correcta
    return(contraseña_correcta)
       
#asignamos la variable que devuelven las funciones a nuevas variables
nombre_correcto = fun_nombre(lista_nombres)
contraseña_correcta = fun_contraseña(nombre_correcto, lista_contraseñas)

print("---------------------")

#si el nombre_correcto no esta vacio entra al if para imprimir las credenciales
if nombre_correcto != "":
    #si la contraseña tiene menos de 4 caracteres se imprime "****"
    if len(contraseña_correcta) <= 4:
        print("Usted ingresara con las siguientes credenciales:")
        print("Nombre de usuario:", nombre_correcto)
        contraseña_oculta = "*" * len(contraseña_correcta)
        print("Contraseña:", contraseña_oculta)
    elif contraseña_correcta == "Contraseña Incorrecta":
        print("Usuario bloqueado. Ponganse en contacto con un agente.") 
    else:
        #si la contraseña tiene mas de 4 caracteres, los ultimos 4 se reemplazan por un "*"
        print("Usted ingresara con las siguientes credenciales:")
        print("Nombre de usuario:", nombre_correcto)
        contraseña_oculta = contraseña_correcta[:-4] + "*" * 4
        print("Contraseña:", contraseña_oculta)
#si nombre correcto esta vacio no podra ingresar 
elif nombre_correcto == "":
    print("No podra ingresar.")
