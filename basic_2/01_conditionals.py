#Usaremos estructuras condicionales para ejecutar codigo dependiendo si se cumple o no las condiciones establecidas

PASSWORD = "123456"
contrasenia = input("Introduce tu contrasenia: ")

if(contrasenia == PASSWORD):
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta")


"""------------------------------------"""

#Tambien podemos usar el operador elif para agregar mas condicionales a nuestro código, con el and para agregar mas de una condicion a la vez y con el or para indicar que se cumpla una de las condiciones

number = int(input("Ingrese un numero del 1 al 10 para catalogarlo:"))
if(number < 1):
    print("El numero no corresponde al rango y puede ser negativo o cero")
elif(number > 1 and number <10 ):
    print(f"El numero {number} es menor que 10 y mayor que 1")
elif(number == 5 or number == 10):
    print(f"El numero {number} es multiplo de 5")
else:
    print("El numero no corresponde al rango y es mayor que 10")
    
# Se pueden utilziar estructuras condicionales sin la necesidad del else o elif
edad = int(input("Ingrese su edad: "))
if(edad >= 18):
    print("Eres mayor de edad")
elif(edad < 18 and edad > 0):
    print("Eres menor de edad")