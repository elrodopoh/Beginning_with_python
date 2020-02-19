import S6_funciones_1 as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("!Hola ",nombre,"! Bienvenido/a a la red social más espectacular: Rodo Social Net")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habia un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado, muro) = Red.leer_usuario(nombre)
else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (metros, centimetros) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    interes = Red.obtener_interes()
    pais = Red.obtener_pais()
    ciudad = Red.obtener_ciudad()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aqui ya conocemos los datos del usuario
print("Muy bien, tu perfil cuenta con los siguientes datos:")
Red.mostrar_perfil(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (metros, centimetros) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        interes = Red.obtener_interes()
        pais = Red.obtener_pais()
        ciudad = Red.obtener_ciudad()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos)

    elif opcion == 5:
        print("Has decidido cambiar de usuario y tu perfil se guardara en ",nombre + ".user")
        Red.escribir_usuario(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado, muro)
        print("--------------------------------------------------")
        nombre = Red.obtener_nombre()
        print("!Hola ", nombre, "! Bienvenido a la red social más espectacular: Rodo Social Net")
        if Red.existe_archivo(nombre + ".user"):
            # Esto lo hacemos si ya habia un usuario con ese nombre
            (nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado) = Red.leer_usuario(nombre)
        else:
            print()
            edad = Red.obtener_edad()
            (metros, centimetros) = Red.obtener_estatura()
            sexo = Red.obtener_sexo()
            interes = Red.obtener_interes()
            pais = Red.obtener_pais()
            ciudad = Red.obtener_ciudad()
            amigos = Red.obtener_lista_amigos()
            estado = ""
            muro = []

    elif opcion == 6:
        amigos.append(input("¿Que amigo deseas agregar a tu lista? "))
        #Red.escribir_usuario(amigos) # Te faltan varaibles en esta llamada de funcion
        print("---------------- LISTA DE AMIGOS -----------------")
        print(*amigos, sep='\n')
        print("--------------------------------------------------")

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, metros, centimetros, sexo, interes, pais, ciudad, amigos, estado, muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar la mas espectacular red social: Rodo Social Net. ¡Hasta pronto!")
