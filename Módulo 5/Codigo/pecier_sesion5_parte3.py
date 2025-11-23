# -*- coding: utf-8 -*-
"""

# Día 5 Parte 3: Carga de datos reales

## Ejemplos

**Ejemplo 5.12:**
 Carga de datos reales
"""

import pandas as pd

tensiones = pd.read_csv('tensiones.csv', parse_dates=['fecha'], index_col='fecha')
print(tensiones.head())

"""**Ejemplo 5.13:** Promedio de una columna"""

print(tensiones['tension1'].mean())

"""**Ejemplo 5.14:** Desviación estándar de columna"""

print(tensiones['tension1'].std())

"""**Ejemplo 5.15:** Valor máximo y momento en que ocurre"""

print(tensiones['tension1'].max())

print(tensiones['tension1'].idxmax())

"""**Ejemplo 5.16:** Categorización de valores"""

df_backup = tensiones.copy()  # recomendación antes de eliminar columnas


media = tensiones['tension1'].mean()
std = tensiones['tension1'].std()

def clasificar_voltaje(v):
    if v < media - std:
        return 'Bajo'
    elif v > media + std:
        return 'Alto'
    else:
        return 'Medio'

tensiones['Nivel Voltaje 1'] = tensiones['tension1'].apply(clasificar_voltaje)

print(tensiones)

"""**Ejemplo 5.17:** Clasificación con NumPy: `np.where()`"""

import numpy as np
tensiones['Voltaje Seguro 1'] = np.where(tensiones['tension1'] < 120, 'Sí', 'No')

"""## Ejercicios

**Ejercicio 5.9:**
 Para los datos contenidos en la columna tension2, determine:

 a) Valor máximo y fecha en que ocurre
"""

# Espacio para resolver el ejercicio

"""b) Repita el Ejemplo 5.16 para la columna tension2."""

# Espacio para resolver el ejercicio

"""c) Repita el Ejemplo 5.17 para la columna tension 2."""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.10:** Establezca una columna que se llama "Reporte", en la cual se consigne si la tensión en las columnas tension1 y tension2 tuvieron un valor bajo 119. Sugerencia: Ver Ejemplo 5.5"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.11:** Analice la diferencia que existe entre utilizar:

`print(tensiones['tension1'].mean())`

y


print(tensiones['tension1'].mean) [texto del vínculo](https://)
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.12:**
 Para los datos contenidos en la columna tension2, determine:

 a) Valor mínimo y fecha en que ocurre
"""
