#------------------
# SLICING
#------------------
# uiere decir "rebanar" en español, e indica si queremos separa una parte de una lista de una lista mas grande

list_of_animals = ["perro", "gato ", "dinosaurio", "cuervo", "conejo"]
# De la siguiente lista se solicita hallar los animales que camninan en 4 patas, usar slicing:
animals_with_four_legs = list_of_animals[:2]
animals_with_four_legs.extend(list_of_animals[4:5])
print(animals_with_four_legs)

favorite_foods = ["tequeños", "empanadas", "lasagna", "papitas", "wantan", "sushi"]
# De la siguiente lista se solicita hallar los alimentos que son fritos, usar slicing:
#identificamos el indice de los alimentos que son fritos, que vendrian a ser el 0, el 3 y el 4, entonces
fried_foods = favorite_foods[0:1]
fried_foods.extend(favorite_foods[3:5])
print(fried_foods)

