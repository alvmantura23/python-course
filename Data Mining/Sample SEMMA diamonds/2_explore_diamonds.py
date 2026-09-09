""" ====================================================
    METODOLOGIA SEMMA: FASE 2 - EXPLORACION DE LOS DATOS
    ====================================================
    Aprenderemos a analizar estadisticas, detectar nulos y entender variables categóricas
"""

import pandas as pd

# cargamos el dataset
data = pd.read_csv("./diamonds/diamonds.csv")

# describe() : describe columnas numericas el promedio, mínimo, máximo y desviación estanddar (mean : media, std: desviacion estandar (que tanto se aleja del promedio si es bajo entonces los valores son parecidos al promedio, si es alto hay mucha variedad ejemplo precios), por ultimo x, y y z son los percentiles)
print("\nDescribiendo la cantidad, el promedio, la desviacion estandar, el minimo, los percentiles y el maximo")
print(data.describe())
"""
Unnamed: 0         carat         depth         table         price             x             y             z
count  53940.000000  53940.000000  53940.000000  53940.000000  53940.000000  53940.000000  53940.000000  53940.000000
mean   26970.500000      0.797940     61.749405     57.457184   3932.799722      5.731157      5.734526      3.538734
std    15571.281097      0.474011      1.432621      2.234491   3989.439738      1.121761      1.142135      0.705699
min        1.000000      0.200000     43.000000     43.000000    326.000000      0.000000      0.000000      0.000000
25%    13485.750000      0.400000     61.000000     56.000000    950.000000      4.710000      4.720000      2.910000
50%    26970.500000      0.700000     61.800000     57.000000   2401.000000      5.700000      5.710000      3.530000
75%    40455.250000      1.040000     62.500000     59.000000   5324.250000      6.540000      6.540000      4.040000
max    53940.000000      5.010000     79.000000     95.000000  18823.000000     10.740000     58.900000     31.800000
"""

# .isnull().sum() se usa para contar datos nulos , para saber si eso puede arruinar futuros análisis (muy util)
print("\n", data.isnull().sum())
""" exit
    Unnamed: 0    0
    carat         0
    cut           0
    color         0
    clarity       0
    depth         0
    table         0
    price         0
    x             0
    y             0
    z             0
""" 

# Una columna de todas las instancias de la tabla tienen valores (categoricos, numericos , ..) pero lo importante es saber cuanto de cada tipo
# Entonces usamos value_counts() Ejemplo: "cut" que por revision manual puede tener very good, good, fair ,.. 

# Para saber cuantos hay de cada uno
print(f"\nAnalizando tipo de dato categórico para variable corte[cut] \n {data["cut"].value_counts()}")
""" exit
    cut
    Ideal        21551
    Premium      13791
    Very Good    12082
    Good          4906
    Fair          1610
"""

# grouphy()[].mean() : Indica que tanto influye una variable en otra (Ej: "cut" y "price")
print("\nVerifiquemos si el tipo de corte influye directamente en el precio ?")
print(data.groupby("cut")["price"].mean())
"""
    Fair         4358.757764
    Good         3928.864452
    Ideal        3457.541970
    Premium      4584.257704
    Very Good    3981.759891

    Descubrimiento: El corte ideal tiene el corte mas bajo : ¿Por que? Piezas de diamante ideal son mas pequeñas, por lo tanto menos quilates
"""
