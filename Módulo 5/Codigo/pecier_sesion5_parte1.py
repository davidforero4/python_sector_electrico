# -*- coding: utf-8 -*-
"""
# Día 5 Parte 1: Introducción a Pandas

## Ejemplos

**Ejemplo 5.1:** Serie de valores
"""

import pandas as pd
mediciones_voltaje = pd.Series([220.5, 221.3, 219.8, 220.2],

                                name='Voltaje (V)',
                                index=['08:00', '09:00', '10:00', '11:00'])

print(mediciones_voltaje)

"""**Ejemplo 5.2:** DataFrame simple"""

import pandas as pd

df = pd.DataFrame({
    'Voltaje (V)': [220, 221, 219, 222],
    'Corriente (A)': [10, 9.5, 10.5, 11],
    'Potencia (W)': [2200, 2100, 2300, 2442]
}, index=['08:00', '09:00', '10:00', '11:00'])

print(df)

"""**Ejemplo 5.3:** Selección de valores con .loc"""

# Seleccionar una fila por etiqueta
df.loc['09:00']

# Seleccionar varias filas por etiquetas
df.loc[['09:00', '10:00']]

# Seleccionar una columna
df.loc[:, 'Corriente (A)']

# Seleccionar rango de filas y columnas
df.loc['09:00':'11:00', 'Voltaje (V)':'Potencia (W)']

# Seleccionar varias columnas
df.loc[:, ['Voltaje (V)', 'Potencia (W)']]

"""*Nota:* Cuando usas rangos en `.loc`, **el último valor sí se incluye**.

**Ejemplo 5.4:** Selección de valores con .iloc
"""

# Fila en posición 1 (segunda fila)
df.iloc[1]

# Filas 1 y 2 (excluye la posición final 3)
df.iloc[1:3]

# Primera columna (posición 0)
df.iloc[:, 0]

# Primera y segunda columna
df.iloc[:, 0:2]

# Filas 1 a 3 y columnas 1 a 2
df.iloc[1:4, 1:3]

"""*Nota:* En `.iloc`, **los rangos se comportan como en Python estándar**: el extremo superior **no se incluye**.

## Ejercicios

**Ejercicio 5.1:**

Crea una Serie que registre la temperatura de un transformador cada 30 minutos. Usa los siguientes índices: `'00:00'`, `'00:30'`, `'01:00'`, `'01:30'`.
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.2:**

Crea un DataFrame con 5 registros horarios (`06:00` a `10:00`) con columnas: `Fase R (V)`, `Fase S (V)`, `Fase T (V)`, `Corriente (A)`.
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.3:**

Usando el DataFrame `df` anterior:

1. Usa `.loc` para obtener:

   * La fila correspondiente a `'10:00'`
   * Las columnas `'Corriente (A)'` y `'Potencia (W)'`
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.4:** Usa `.iloc` para:

   * Obtener las filas 0 y 1
   * Obtener el valor de la fila 2 y columna 0
"""

# Espacio para resolver el ejercicio
