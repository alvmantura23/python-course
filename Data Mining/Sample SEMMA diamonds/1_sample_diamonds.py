""" ====================================================
    METODOLOGIA SEMMA: FASE 1 - SAMPLE
    ====================================================
    Aprenderemos a cargar los datos de un archivo .csv , mostrar la tabla cargada para n filas, mostrado de n filas aleatorias y contar el # de filas y columnas y saber los tipos de datos de la tabla 
"""
import pandas as pd

n = 10

# Vamos a cargar el conjunto de datos de nuestro negocio con read_csv()
data = pd.read_csv("./diamonds/diamonds.csv")

# Mostrar las 10 primeras filas con head()
print(data.head(n))

# info() : nos permite obtener un resumen del archivo (#filas, #columnas)
print("Mostrando resumen del archivo diamonds.csv")
data.info()

# shape() : Para saber cuantas filas y columnas tiene mi tabla
print(f"Mostrando #filas y #columnas {data.shape}")

# sample() : Nos da una muestra aleatoria de n filas, al azar (util para varificar al azar)
print("Mostrando 10 filas seleccionadas aleatoriamente con .sample()")
print(data.sample(n))