#Para ingresar uan palabra y ejecutar en la terminal se usa la funcion input() y se le puede agregar un mensaje para que el usuario sepa que debe ingresar

#Run python file in Dedicated Terminal: Ctrl + Shift + P -> Run Python File in Terminal
nombre = input("Ingresa su nombre: ")
print(f"Su nombre es: {nombre}")

# Todo lo que se ingrese por el input se guardara como una cadena de String, incluso si se trata de un numero

supuesto_numero = input("Ingresa un numero: ")
print(f"El numero {supuesto_numero} ingresado es del tipo: {type(supuesto_numero)}")

#Si queremos ingresar un valor y trabajarlo como otro tipo que no sea string vamos a tener que castearlo o convertirlo en otro tipo ejemplo un numero entero o un numero decimal
edades = int(input("Ingresa tu edad: "))
print(f"Tu edad es:{edades} y el tipo es: {type(edades)}")

#Si queremos ingresar mas de un elemento por por el input vamos a utilzar el metodo split() para separar los elementos por un espacio y guardarlas en una lista

dia, mes , anio = input("Ingresa el dia, el mes y el año de tu nacimiento: ").split()
print(f"Tu dia es {dia}, tu mes es {mes}, tu anio es {anio}")


#Si queremos ingresar el mismo elemento a un conjunto de variables vamos a utilizar el operador de asignacion multiple
x = y = z = input("Ingresa un valor para guararlos en x, y y z:")
print(f"El valor de x es: {x} el valor de y es: {y} y el valor de z es: {z}")

