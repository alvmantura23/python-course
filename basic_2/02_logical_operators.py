#Los operadores logicos permiten combinar varias condiciones para obtener un resultado booleano.
#Los operaadores logicos con : and , or y not

# ================================================================
## and:
# Devuelve True si todas las condiciones son verdaderas, de lo contrario devuelve false
# ================================================================

"""Identificador de Votante"""
age = int(input("Ingrese su edad porfavor: "))
citizenship = input("¿Eres peruano? (si/no): ")

if (age >= 18 and age <= 65 and citizenship == "si"):
    print("Eres elegible para votar.")
else:
    print("No eres elegible para votar.")

del age, citizenship  #eliminamos las variables para evitar conflictos con el siguiente ejemplo

# ================================================================
## or:
# Debuelve True si al menos una condicion es verdadera sino devuelve false
# ================================================================

"""Identificador de candidato a la presidencia"""
age = int(input("Ingrese su edad porfavor: "))
citizenship = input("¿Eres peruano? (si/no): ")
residence_time = int(input("¿Cuantos años lleva residiendo en Perú? "))

if (age > 35 and citizenship == "si" and residence_time >= 10):
    print("Eres elegible para ser candidato a la presindecia.")
elif(age > 35 and citizenship == "si" or residence_time < 10):
    print("Eres ciudadano votante pero no eres elegible para ser candidato a la precidencia.")
else:
    print("No eres elegible para votar ni para ser candidato a la presidencia.")


# ================================================================
# not:
# Devuelve el valor opuesto a una condicion, es decir si la condicion es True devuelve false y si la condicion es false devuelve True
# ================================================================

"""Identificador de partido politico elegible"""

partido = input("¿Cual es tu partido politico?: ") #example: chavismo
if (not (partido == "chavismo")):
    print(f"Tu partido politico es el {partido} el cual si es elegible para las elecciones.")
else:
    print(f"Tu partido politico es el {partido} el cual no es elegible para las elecciones.")
