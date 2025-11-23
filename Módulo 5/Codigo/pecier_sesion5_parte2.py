# -*- coding: utf-8 -*-
"""

# Día 5 Parte 1: Introducción a Pandas - DataFrames y Series

## Ejemplos

**Ejemplo 5.4:** Filtrado de datos
"""

import pandas as pd

df = pd.DataFrame({
    'Voltaje (V)': [220, 221, 219, 222],
    'Corriente (A)': [10, 9.5, 10.5, 11],
    'Potencia (W)': [2200, 2100, 2300, 2442]
}, index=['08:00', '09:00', '10:00', '11:00'])

print(df)

df[df['Voltaje (V)'] > 220]

"""**Ejemplo 5.5:** Filtrado de datos con dos condiciones"""

condicion = (df['Voltaje (V)'] > 219) & (df['Corriente (A)'] < 11)

df[condicion]

"""**Ejemplo 5.6:** Estadísticas básicas"""

df.describe()

"""**Ejemplo 5.7:** Operaciones estadísticas"""

print(f"Voltaje promedio: {df['Voltaje (V)'].mean():.2f} V")

print(f"Potencia máxima: {df['Potencia (W)'].max()} W")

"""**Ejemplo 5.8:** Agregar columnas


"""

df["Voltaje escala"] = df['Voltaje (V)']*1000
print(df)

"""**Ejemplo 5.9:** Eliminar columnas"""

df.drop(columns=['Voltaje escala'], inplace=True)
print(df)

"""## Ejercicios

**Ejercicio 5.5:**

Crea un DataFrame con 5 registros horarios (06:00 a 10:00) con columnas: Fase R (V), Fase S (V), Fase T (V), Corriente (A)
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.6:**

Agregue una columna con el promedio de los voltajes del dataframe anterior.
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.7:**

Filtre las filas donde el voltaje la potencia supere 2300 W.


"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.8:**

Encuentra registros con corriente > 10 A y voltaje < 220 V.



"""

# Espacio para resolver el ejercicio
