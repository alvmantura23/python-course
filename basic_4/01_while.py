# ----------------------
# WHILE
# ----------------------
# Permite ejecutar un bloque de código repetidamente mientras se cumpla una condición

# Ejercicio: Identificar y guardar en una lista los multiplos de 5 menores que 100
count = 0
numbers = []

while(count < 100):
    if(count % 5) == 0:
        print(f"Insertando elemento: {count}")
        numbers.append(count)
    count += 1

del count, numbers # Para la buena gestion de memoria :)

# ----------------------
# WHILE y BREAK
# ----------------------
# Se encarga de finalizar la ejecucion del ciclo inmediatamente y salir de ella, incluso si la condicion principal del while sigue siendo verdadera

# Ejercicio: Tenemos una lista que ha excedido su tamaño maximo de elementos, en este caso se nos solicita ir eliminado elementos hasta que la lista quede con 15 elementos, imprimir los 15 elementos al final

# Primero simularemos el llenado la lista
count = 0
numbers = []
while count < 100:
    numbers.append(count)
    count += 1

# Segundo vamos a reduciendo la lista, quitando elementos
while True:
    numbers.pop()
    if len(numbers) == 15:
        break

# Tercero  vamos a mostrar la lista
print("\n", numbers)

del count, numbers # Para la buena gestion de memoria

# ----------------------
# WHILE y CONTINUE
# ----------------------
# Cntinue, nos permite saltarnos la iteracion del bucle en la que nos encontramos actualmente

# Ejercicio: Se pide crear una lista de 100 numeros y conforme se vaya insertando los numeros identificar cada numero multiplo de 3 y de 5 e ir eliminandolo

count = 0
numbers = []

while count < 100: # 0
    count += 1 #1
    if count % 3 == 0 or count % 5 == 0:
        continue
    numbers.append(count)
print(numbers)


