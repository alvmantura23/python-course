#----------------
# Lists [] in Python
#----------------

#Characteristics of lists: []
# Las listas son estructuras de datos que nos permiten guardar mas de un valor en una sola variable
# Son altamente flexibles, ya que pueden contener diferentes tipos de datos (numeros, cadenas, booleanos, listas, etc)
# Se pueden MODIFICAR luego de haberse creado ---> MUTABLES

list_of_numbers = [1,2,3,4,5]
ingredients_of_a_cake = ["huevo", "leche", "mantequilla", "harina"]
empty_list = []

data_list = ["Alvaro", "Cueva", 25, 1.66, True]

print(list_of_numbers)
print(ingredients_of_a_cake)
print(empty_list)
print(data_list)

"""Acceso a elementos de las listas"""

# Las listas van a tener indices numericos que val del cero hasta la poscion menos 1

# Ejemplo de las listas anteriomente creadas

#list of numbers
a = list_of_numbers[0]
b = list_of_numbers[1]
c = list_of_numbers[2]
d = list_of_numbers[3]
e = list_of_numbers[4]

print(f"La lista es la siguiente: {list_of_numbers} el primer elemento es {a}, el segundo es {b}, el tercero es {c}, el cuarto es {d}, el quinto es {e}")


del list_of_numbers

#print(f"La lista de numero esta vacia ahora {list_of_numbers}") #me va a botar un error porque la lista , la estructura de datos list of numbers ha sido borrada

# Ordenamiento de Listas
books = ["Lidersheeps", "La pasion de Jerry", "El principito", "Harry Potter"] 
list_of_numbers = [7,3,5,9,1,20]
print(type(books)) # Class list
print(sorted(books)) # ['El principito', 'Harry Potter', 'La pasion de Jerry', 'Lidersheeps']
print(sorted(list_of_numbers))

# Ordenamiento de la lista en orden invertido de menor a mayor
print(sorted(list_of_numbers, reverse= True))

new_list_of_numbers = [23, 85, 4, 42, 71, 15, 99, 36, 58, 12]
#Que pasaria si me piden, ordename esa lista de numeros de forma invertida de mayor a menor , entonces:
lista_invertida = sorted(new_list_of_numbers, reverse = True)
print(lista_invertida)

# -----------------
# AGREGAR ELEMENTOS
# -----------------

books.append("Pirates of the Caribbean")
print(books)

# -----------------
# AGREGAR ELEMENTOS EN UNA POSICION ESPECIFICA
# -----------------

days_of_week = ["Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Lista Original
print(days_of_week)
# Para insertar un elemento en una posicion especidica de la lista vamos a usar la funcion "insert" , el cual recibe 2 argumentos, el primero es la posicion o indice de la lista y el segundo es el elemento a insertar
days_of_week.insert(1, "Tuesday")
print(days_of_week)

# -----------------
# AGREGAR UNA LISTA DE ELEMENTOS AL FINAL DE UNA LISTA
# -----------------

pokemon_list = ["Pikachu", "Raichu", "Garadous", "Charizard"]
#Agregar a la list original una lista con los pokemones "Magikard" y "Deoxys"
pokemon_list.extend(["Magikarp", "Deoxys"])
print(pokemon_list)

# -----------------
# CONOCER EL INDICE DE UN ELEMENTO DE UNA LISTA
# -----------------

my_favorites_djs = ["Martin Garrix", "Kygo", "David Guetta", "KSMR", "Deadmau5"]
#quiero que me identifiques el indice del dj que compuso la cancion "Stole the Show"
index = my_favorites_djs.index("Kygo")
print(f"El indice del dj que compuso la cancion es {index}")

# -----------------
# CONOCER EL TAMAÑO DE UNA LISTA
# -----------------

my_favorite_bands = ["Coldplay", "Imagine Dragons", "Ha Ash", "Green Day"]
#Determinar el tamaño de la lista my_favorite_bands
size = len(my_favorite_bands) #devuelve un entero
print(f"El tamaño de la lista es {size}")