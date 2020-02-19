import os

def mostrar_bienvenida():
    print("¡Bienvenido/a a la mas espectacular red social!:")
    print("""
        ____            __       _____            _       __   _   __     __ 
       / __ \____  ____/ /___   / ___/____  _____(_)___ _/ /  / | / /__  / /_
      / /_/ / __ \/ __  / __ \  \__ \/ __ \/ ___/ / __ `/ /  /  |/ / _ \/ __/
     / _, _/ /_/ / /_/ / /_/ / ___/ / /_/ / /__/ / /_/ / /  / /|  /  __/ /_  
    /_/ |_|\____/\__,_/\____/ /____/\____/\___/_/\__,_/_/  /_/ |_/\___/\__/
                                       
    ¡|(•◡•)|, (❍ᴥ❍ʋ), | |[•◡•]| Finn, Jake & BMO te dan la bienvenida!
    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas: ")
    return nombre
def obtener_edad():
    agno = int(input("Para preparar tu perfil te hare unas breves preguntas, primero dime en que año naciste. "))
    edad = 2020 - agno - 1
    return edad
def obtener_estatura():
    estatura = float(input("¿Cuanto mides? Ingresa los datos en metros. Ejemplo: 1.70 :   "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)
def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo
def obtener_interes():
    interes = input("Estas interesado/a en conocer M=Mujeres, H=Hombres: ")
    while interes != 'M' and interes != 'H':
        interes = input("Estas interesado/a en conocer M=Mujeres, H=Hombres: ")
    return interes
def obtener_pais():
    pais = input("Ahora dime de que país eres:  ")
    return pais
def obtener_ciudad():
    ciudad = input("Tambien tu ciudad natal:  ")
    return ciudad
def obtener_lista_amigos():
    linea = input("Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos

def mostrar_perfil(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", metros, "metro y", centimetros, "centimetros")
    print("Sexo (M=Masculino, F=Femenino): ", sexo)
    print("Interesado/a en conocer (M=Mujeres, H=Hombres): ", interes)
    print("Pais:    ", pais)
    print("Ciudad:  ", ciudad)
    print("Amigos:  ", len(amigos))
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje publico")
    print("  2. Mostrar mi muro")
    print("  3. Mostrar los datos de tu perfil")
    print("  4. Actualizar tu perfil de usuario")
    print("  5. Cambiar de usuario")
    print("  6. Agregar un nuevo amigo a tu lista")
    print("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    while opcion < 0 or opcion > 6:
        print("No conozco la opcion que has ingresado. Intentalo otra vez.")
        opcion = int(input("Ingresa una opcion: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Que piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
            print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@" + destinatario, mensaje)
    print("--------------------------------------------------")

def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

#Publica un mensaje en el muro personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", mensaje)
    print("--------------------------------------------------")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    sexo = archivo_usuario.readline().rstrip()
    interes = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    ciudad = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado, muro)

def escribir_usuario(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(metros + centimetros/100)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(interes+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(ciudad+"\n")
    archivo_usuario.write(str(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuaciÃ³n del Ãºltimo estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()
