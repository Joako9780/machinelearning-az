# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 22:49:18 2025

@author: Joaco Becerra
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Datos de ejemplo
df = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde'],
    'tipo':  ['A', 'B', 'A'],
    'precio': [10, 15, 12]
})

# Definimos las transformaciones
ct = ColumnTransformer(
    transformers=[
        ('cod_color', OneHotEncoder(), ['color']),
        ('cod_tipo',  OneHotEncoder(), ['tipo']),
        ('escala_precio', StandardScaler(), ['precio'])
    ],
    remainder='drop'
)

# Ajustamos y transformamos
X_trans = ct.fit_transform(df)

print(ct.get_feature_names_out())
# → ['cod_color__rojo', 'cod_color__azul', 'cod_color__verde',
#    'cod_tipo__A',   'cod_tipo__B',
#    'escala_precio']
print(np.array(X_trans))
