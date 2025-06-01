# -*- coding: utf-8 -*-
# Plantilla de Pre Procesado de Datos

# Importar librerias
# Con as le damos un alias mas corto para referenciar la libreria

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
# Para cargar los datos estos se guardan en una variable

dataset = pd.read_csv("Data.csv")

# Se crean matriz de variables independientes y vector de variables dependientes
# iloc sirve para localizar los elementos (filas y clmns) de un dataset | index localization
# : significa desde el principio hasta el final, :-1 todas menos la ultima | iloc[filas, clmns]
# values fn que indica que se quiere tomar los valores dentro del dataframe, no las posiciones

X = dataset.iloc[:, :-1].values     # X varible ind. | MAYUS porque es matriz
y = dataset.iloc[:, 3].values     # y variable dep. 

Xog = dataset.iloc[:, :-1].values

# Tratamiento de los NAs
# con la sintaxis from especificamos la funcion que queremos importar de la libreria
# Imputer es una clase

from sklearn.impute import SimpleImputer

# missing_values indica como se encuentran en la tabla los datos faltantes
# strategy indica con que vamos a remplazar esos datos, mean es media
# axis es para saber como se calcula esa media, 0 val de las clmns y 1 val de las filas

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")   # creamos el obj imputer
imputer = imputer.fit(X[:, 1:3])    # usamos este obj para arreglar la matriz X donde estan los nan
                                    # en python el limite superior no se toma, es del 1 al 2
                                    # aplicamos fit para aplicar una funcion a un obj que queremos arreglar en este caso X
X[:, 1:3] = imputer.transform(X[:, 1:3])    # aplicamos la media a todos los datos seleccionados










