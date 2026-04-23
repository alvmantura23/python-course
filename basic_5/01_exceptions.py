# ----------------------
# TRY - EXCEPT
# ----------------------
# Se encarga de controlar el error para evitar que se vea interrumpida la ejecucion del programa

'''
# Ejemplo SUMA DE NUMEROS SIN EXCEPCION CONTROLADA
first_number = int(input("Ingrese primer número: "))
second_number = int(input("Ingrese segundo número: ")) #vamos a ingresar una cadena
suma = first_number + second_number
print(f"La suma es: {suma}") # si ingresamos una cadena como se nos indicó , nos dara un error y se detendra el programa
'''

# Ejemplo de programa con entrada CON EXCEPCION CONTROLADA
try:
    first_number = int(input("Ingrese el primer número: "))
    second_number = int(input("Ingrese el segundo número: "))
    suma = first_number + second_number
    print(f"La suma es {suma} ")
except:
    print("Excepcion encontrada, porfavor ingresa solo numeros!")
print("y continuando con la ejecucion del programa...")

# Ejercicio: Se le pide al usuario hacer un programa que nos permita autenticar si la contraseña ingresada es correcta, el usuario tiene como máximo 3 intentos si llega a exceder el tercer intento el programa debera mostrar el mensaje bloqueando credenciales
PASSWORD = 2026
count = 0
while count<3:
    try:
        password_number = int(input("Ingrese la contraseña que es un número: "))
        if password_number == PASSWORD:
            print("La contraseña ingresada es la correcta :)")
            break
        else:
            count += 1
    except:
        print("La contraseña debe ser un número!!!")
    if (count>=3 and password_number != 2026):
        print("Excediste el numero de intentos")