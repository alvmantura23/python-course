""" ====================================================
    Metodología SEMMA - Fase 4: MODEL (Modelado)
    ====================================================
    Objetivo: Entrenar un modelo de Inteligencia Artificial para predecir precios basados en los quilates.
"""
import pandas as pd
from sklearn.model_selection import train_test_split # Divisdir el conjunto de datos (entrenamiento - prueba) permite usar el train_test_split
from sklearn.linear_model import LinearRegression

print("Iniciando Fase: Modelado")

# 1. Carguemos el dataset modificado
data = pd.read_csv("./diamonds/diamonds.csv")

# 2. Separamos las variables
x = data[["carat"]] # Lo que el modelo espera recibir una matriz/tabla  [[quilates]]
y = data["price"]   # Lo que el modelo espera predecir                  [precio]

# 3. Separamiento de datos (entrenamiento(train = 80%) & prueba (test = 20%))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

print(f"Diamantes usados para entrenar {len(x_train)}")
print(f"Datos usados para pruebas {len(x_test)}\n")

# 4. Crear y entrenar el modelo
modelo = LinearRegression()
print("Entrenando el modelo ")
modelo.fit(x_train, y_train)
print("Modelo entrenado ")

# PASO EXTRA: Poner a prueba la Inteligencia Artificial
#Para ello vamos a inventar un diamante neuvo de 1.5 quilates para ver cuanto calcula el precio
quilates_nuevos = [[1.5]]
print(f"Prediccion un diamante nuevo de 1.5 quilates deberia costar {modelo.predict(quilates_nuevos)}")