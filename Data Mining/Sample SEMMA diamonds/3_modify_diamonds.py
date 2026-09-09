""" ====================================================
    METODOLOGIA SEMMA: FASE 3 - Modify
    ====================================================
    Aprenderemos a preparar, limpiar y transformar el dataset
"""
import pandas as pd

# Cargar el dataset en una tabla por nombre data
data = pd.read_csv("./diamonds/diamonds.csv")

# Inventamos una columna llamada "precio_por_quilate" en la tabla data
data["precio_por_quilate"] = data["price"] / data["carat"]

# mostrando tabla con nueva columna "precio_por_quilate" , un solo corchete para sacar una columna suelta []
print(data["precio_por_quilate"].head(20))

# Usando 2 corchetes para extraer una subtabla
print(data[["price", "carat", "precio_por_quilate"]].head(20))
"""
price  carat  precio_por_quilate
0     326   0.23         1417.391304
1     326   0.21         1552.380952
2     327   0.23         1421.739130
3     334   0.29         1151.724138
4     335   0.31         1080.645161
5     336   0.24         1400.000000
6     336   0.24         1400.000000
7     337   0.26         1296.153846
8     337   0.22         1531.818182
9     338   0.23         1469.565217
10    339   0.30         1130.000000
11    340   0.23         1478.260870
12    342   0.22         1554.545455
13    344   0.31         1109.677419
14    345   0.20         1725.000000
15    345   0.32         1078.125000
16    348   0.30         1160.000000
17    351   0.30         1170.000000
18    351   0.30         1170.000000
19    351   0.30         1170.000000
"""

# Imaginemos qu queremos agrupar los tipos de una variable para saber cuantos hay de acda uno, usamos grouphy("variable")
print("\nSe está calculando el valor real promedio por unidad de peso (precio por quilate) para demostrar que los diamantes con mejor calidad de corte sí son los más caros.")
metrica_justa = data.groupby("cut")["precio_por_quilate"].mean()
print(metrica_justa) # Con mean calculamos el promedio por quilate


# Guardado de datos modificados
data.to_csv("./diamonds/diamonds_modificado.csv", index=False)  # Pandas por defecto, crea una columna de indices(index) al ponerle false le decimos que no guarde esa columna de indices ya que la tabla data ya tenia esa columna indices
print("¡Archivo diamonds_modificado.csv guardado exitosamente!")