#----------------
# LISTAS []
#----------------

#Characteristics of lists: []
# Las listas son estructuras de datos que nos permiten guardar mas de un valor en una sola variable
# Son altamente flexibles, ya que pueden contener diferentes tipos de datos (numeros, cadenas, booleanos, listas, etc)
# Se pueden MODIFICAR luego de haberse creado ---> MUTABLES

list_of_numbers = [1,2,3,4,5]
ingredients_of_a_cake = ["huevo", "leche", "mantequilla", "harina"]
empty_list = []
data_list = ["Alvaro", "Cueva", 25, 1.66, True]

print("List of numbers: ", list_of_numbers)
print("Ingredients of a cake: ", ingredients_of_a_cake)
print("Empty list: ", empty_list)
print("Lista de estructura de datos: ", data_list, "\n")

"""Acceso a elementos de las listas"""

# Las listas van a tener indices numericos que van del cero(0) hasta el numero de elementos disminuido en 1 (posicion-1)
# Ejemplo de las listas anteriomente creadas

#list of numbers
a = list_of_numbers[0] 
b = list_of_numbers[1]
c = list_of_numbers[2]
d = list_of_numbers[3]
e = list_of_numbers[4]

print(f"La lista es la siguiente: {list_of_numbers} \nDonde:")
print(f"el primer elemento es {a}")
print(f"el segundo elemento es {b}")
print(f"el tercer elemento es {c}")
print(f"el cuarto elemento es {d}")
print(f"el quinto elemento es {e}\n")


del list_of_numbers

#print(f"La lista de numero esta vacia ahora {list_of_numbers}") #me va a botar un error porque la lista , la estructura de datos list of numbers ha sido borrada

#-------------------
# ORDENAMIENTO DE LISTAS
#-------------------

books = ["Lidersheeps", "La pasion de Jerry", "El principito", "Harry Potter"] 
list_of_numbers = [7,3,5,9,1,20]

print("Lista de libros: ", books)
print("Clase de lalista de libros: ", type(books)) # Class list
print("Lista de libros ordenada", sorted(books), "\n") # ['El principito', 'Harry Potter', 'La pasion de Jerry', 'Lidersheeps']

print("Lista desordenada original: ", list_of_numbers)
print("Lista ordenada con la funcion sorted: ", sorted(list_of_numbers))
print("Lista ordenada inversamente de mayor a menor: ", sorted(list_of_numbers, reverse= True), "\n")

#Ordenar la siguiente lista new_list_of_numbers de forma descendente:
new_list_of_numbers = [23, 85, 4, 42, 71, 15, 99, 36, 58, 12]
print("Tenemos la lista: ", new_list_of_numbers)
lista_invertida = sorted(new_list_of_numbers, reverse = True)
print("La lista invertida es: ", lista_invertida, "\n")

# -----------------
# AGREGAR ELEMENTOS AL FINAL DE LA LISTA
# -----------------

books.append("Pirates of the Caribbean")
print("Agregando libro al final de la lista de libros: ", books, "\n")

# -----------------
# AGREGAR ELEMENTOS EN UNA POSICION ESPECIFICA
# -----------------

days_of_week = ["Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Lista Original
print(days_of_week)
# Para insertar un elemento en una posicion especidica de la lista vamos a usar la funcion "insert" , el cual recibe 2 argumentos, el primero es la posicion o indice de la lista y el segundo es el elemento a insertar
days_of_week.insert(1, "Tuesday")
print(f"Insertando {days_of_week[1]} en la posicion [1] en la lista: ", days_of_week, "\n")

# -----------------
# FUSIONAR LISTAS
# -----------------

pokemon_list = ["Pikachu", "Raichu", "Garadous", "Charizard"]
#Agregar a la list original una lista con los pokemones "Magikard" y "Deoxys"
pokemon_list.extend(["Magikarp", "Deoxys"])
print(pokemon_list)

# -----------------
# HALLAR EL INDICE DE UN ELEMENTO DE UNA LISTA
# -----------------

my_favorites_djs = ["Martin Garrix", "Kygo", "David Guetta", "KSMR", "Deadmau5"]
#Quiero que me identifiques el indice del dj que compuso la cancion "Stole the Show"
index = my_favorites_djs.index("Kygo")
print(f"El indice del dj que compuso la cancion es {index}")

# -----------------
# HALLAR EL TAMAÑO DE UNA LISTA
# -----------------

my_favorite_bands = ["Coldplay", "Imagine Dragons", "Ha Ash", "Green Day"]
#Determinar el tamaño de la lista my_favorite_bands
size = len(my_favorite_bands) #devuelve un entero
print(f"El tamaño de la lista es {size}")

# -----------------
# REMOVER EL ELEMENTO DE UNA LISTA
# -----------------

# Ejercicio, crea una lista y remueve el elemento que no corresponde, tu te daras cuenta
superheroes =["Ultraman", "Iron Man", "Sayaman", "Homelander", "Linterna Verde"]
superheroes.remove("Homelander")
print(superheroes, "\n")

# -----------------
# ELIMINAR ELEMENTOS AL FINAL DE UNA LISTA
# -----------------
#El metodo pop() nos permite eliminar el ultimo elemento de una lista y devolvernos el elemento eliminado

'''
Ejercicio: "Simulador de Boton Atras"
Imaginemos que estamos programado un navegador sencillo en el cual tenemos una lista que guarda las paginas que el usuario va visitando. Cuando el usuario pulsa el boton "Atras", el navegador debe eliminar la ultima pagina visitada y mostrar unmensaje diciendo a que pagina esta regresando
'''
web_sites_visited = ["www.google.com", "www.youtube.com/images", "www.youtube.com", "www.youtube.com/watch?v=TkN2i-_4N4g"]
print(f"L lista de sitios visitados es: ", web_sites_visited)
# pulso el boton Atras
sitio_quitado_de_la_lista = web_sites_visited.pop()
print(f"El sitio ´{sitio_quitado_de_la_lista} fue eliminado de la lista: {web_sites_visited}, regresando...")

# -----------------
# CONTAR ELEMENTOS DE UNA LISTA
# -----------------
#De la siguiente lista de letras identificar cuantas veces se repite la letra : a
list_of_letters = ["a", "n", "i", "t", "a", "l", "a", "v", "a", "l", "a", "t", "i", "n", "a"]
print(f"Tenemos la siguiente lista: {list_of_letters}")
print(f"El elemento 'a' se repite: ", list_of_letters.count("a")," veces")
