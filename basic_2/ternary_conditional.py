
# Conditional Ternary Operator
# Es nada mas y menos que escribir el condicional if- else en una sola linea de codigo
# La sintaxis es la siguiente:

numero_ingresado = int(input("Ingrese un numero para determinar si es par o impar:"))
resultado = "el numero es par" if (numero_ingresado%2) == 0 else "el numero es impar"
print(resultado)

#Veamos si se puede utilizar el operador ternario para evaluar mas de una condicion con el elif veamos:

del numero_ingresado, resultado

nombre = input("Ingrese su nombre: ")

nombre_elegido = "Eres fiel" if nombre == "Alvaro" else "Eres infiel" if nombre == "Keneth" else "No eres ni fiel ni infiel"
print(nombre_elegido)