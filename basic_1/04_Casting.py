#Aqui vamos a comvertir un tipo de dato a otro, esto se llama casting
a = 10
print("a:", a, "type is:", type(a))
b = a
print("b:", b, "type is:", type(b)) #deben coincidir en el tipo porque estamos copiando el valor de la variable la cuale s el tipo int

b = float(a) #con esto convertimos el tipo de dato de a a float, es decir, de entero a decimal
print("b:",b, "type is:", type(b))

c = str(a)
print("c:", c, "type is:", type(c)) #con esto convertimos el tipo de dato de a a string, es decir, de entero a cadena de texto

print(int("100") + 200)

d = -1
e = 0
print("d:", bool(d))
print("e:", bool(e))

cadenaVacia = ""
print("cadenaVacia:", bool(cadenaVacia))

