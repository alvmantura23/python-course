'''
Ejercicio: Sistema Gestor de personal para una empresa de transporte

Se nos pide crear un pequeño sistema que tiene por si los siguientes requisitos:
- ✅Existen 2 roles: usuario y administrador
- ✅El sistema debe autenticar la persona que ingresa es usuario o administrador, no otro rol
- Una vez identificado la persona esta podra realizar una serie de acciones las cuales son por roles:
USUARIO
- ✅Debe poder ingresar los siguientes datos (nombre, apellido, dni))
- El nombre apellido y dni deben ser datos correctos (dentro de los parametros)
- El usuario una vez que ingrese los datos, el sistema debe preguntar si los datos ingresados son correctos o no
- Si el usuario responde no , nos debe aparecer un campo el cual nos indique que campo desea cambiar y el usuario debe elegir y cambiar el dato
- ✅Si el sistema pregunta si los datos son correctos y el usuario responde que si, entonces el sistema guardara los datos en una lista
- Una vez que el usuario ingrese sus datos mostrar un mensaje: "Datos guardados"

ADMINISTRADOR
- ✅Tiene un maximo de 3 intentos para ingresar la clave correcta para poder autenticarse
- ✅Debe poder visualizar los datos de los usuarios por un parametro dni
- Debe poder visualizar a todos los usuarios si es que quiere
- Debe poder realizar acciones como los usuarios como: ✅ver sus datos, eliminar o remover usuarios
- ✅Cuando quiera realizar una accion el sistema debe pedir la clave de administrador para validar la accion
'''
#CONST
PASSWORD_ADMIN = "123456"

# VAR
users = []
data_users = []
count_attemps = 0
search = ""
state = True

while (state):
    credential = input("Ingrese su rol porfavor (a:admin / u: user) -> ")
    if(not (credential == "u" or credential == "a")):
        print(f"El rol {credential} no es valido, ingresar rol valido")
    else:
        if(credential == "u"):
            count_attemps += 1
            print("=============")
            print("MENU USUARIO")
            print("=============")

            credential = input("Seleccionar una opcion\nN -> Crear nuevo usuario\nX -> Salir\n=============\nElegir -> ") # Reasignamos la variable, le damso otro valor
            
            if(credential  == "N"):
                #Aqui añadiremos un elemento a la lista
                users.append(count_attemps)

                print(f"User [{count_attemps}]")
                data_users.append(input("Ingresar dni      -> ")) # data_users[1] = dni usuario
                data_users.append(input("Ingresar nombre   -> ")) # data_users[0] = nombre usuario
                data_users.append(input("Ingresar apellido -> ")) # data_users[1] = apellido usuario
                
            else:
                state = False
        else:
            count_attemps = 0 #para dotar al administrador un numero de 3 intentos para ingresar la contrasena dnv
            while(count_attemps<3):
                credential = input("Ingresa su contraseña asignada para continuar -> ") # Reasignacion de la variable credential
                if credential != PASSWORD_ADMIN:
                    count_attemps += 1
                    print(f"Error, le quedan {3-count_attemps} intentos")
                    if (count_attemps == 3):
                        print("Alcanzaste el numero maximo de intentos, cerrando sesion")
                else:
                    print("==================")
                    print("MENU ADMINISTRADOR")
                    print("==================")

                    credential = input("V -> Visualizar Usuarios por DNI\nR -> Remover Usuarios por DNI\nX -> Salir\n==================\nElegir -> ") # Reasignacion de la variable credential

                    if(credential == "V" and len(data_users) != 0):
                        search = input("Ingrese el numero de DNI del usuario: ")
                        if search in data_users:
                            print(f"El usuario por DNI {search}, si se encuentra en la lista")
                            print("==============================================")

                            # reutilizamos el search o podriamos crear otra variable
                            search = data_users.index(search) #ahora search va a tomar el valor del indice del dni
                            print(f"DNI:{data_users[search]}\nNombre: {data_users[search+1]}\nApellido: {data_users[search+2] }") #dni, nombre, apellido
                            print("==============================================")
                            print(count_attemps)
                        else:
                            print("No existe usuario con ese dni")
                    
                    elif (credential == "R"):
                        search = input("Ingrese el numero de DNI del usuario: ")
                        print("")
                    else:
                        if(len(data_users) <= 0):
                            print("La lista de usuarios esta vacia")
                        break
            state = False