# -*- coding: utf-8 -*-
"""

# Día 5 Parte 4: Filtrado, Agrupación y Agregación con Pandas y NumPy

## Ejemplos

**Ejemplo 5.18:** Preparación del Entorno
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # reproducibilidad

n = 48  # 2 días, datos cada hora
fechas = pd.date_range('2023-01-01', periods=n, freq='H')

data = {
    'Timestamp': fechas,
    'Voltaje (V)': np.random.normal(220, 4, n),
    'Corriente (A)': np.random.normal(10, 1.5, n),
    'Fase': np.random.choice(['R', 'S', 'T'], n),
    'Consumo (kWh)': np.random.uniform(1.0, 5.0, n)
}

df = pd.DataFrame(data).set_index('Timestamp')
df.head()

"""**Ejemplo 5.19: Potencia Aparente Estimada**"""

df['Potencia (VA)'] = df['Voltaje (V)'] * df['Corriente (A)']

"""**Ejemplo 5.20 Media Móvil**"""

df['Voltaje_prom_6'] = df['Voltaje (V)'].rolling(window=6).mean()

"""**Ejemplo 5.21: Unión por Índice (`.join()`)**"""

thd = pd.DataFrame({
    'Timestamp': fechas,
    'THD': np.random.uniform(3, 7, n)
}).set_index('Timestamp')

df = df.join(thd)

"""**Para que funcione**:

* Ambos DataFrames deben tener el mismo índice (`DatetimeIndex`).
* Si hay diferencias en los índices, el resultado puede contener `NaN`.

**Ejemplo 5.22: Unión con `merge()`**
"""

mediciones_extra = pd.DataFrame({
    'Timestamp': fechas,
    'Factor_Potencia': np.random.uniform(0.85, 1.0, n)
})

df = df.reset_index().merge(mediciones_extra, on='Timestamp').set_index('Timestamp')

"""**Para que funcione**:

* Las columnas clave deben tener el mismo nombre y tipo.
* Puede usarse `how='left'`, `how='right'` o `how='outer'` según la necesidad.

**Ejemplo 5.23: Extracción Parcial de información de un Dataframe**
"""

df_partes = df[['Voltaje (V)', 'Corriente (A)', 'Fase']]
df_rango = df['2023-01-01 08:00':'2023-01-01 20:00']

"""**Ejemplo 5.24:**

"""

df[df['Corriente (A)'] > 11]

df[(df['Fase'] == 'S') & (df['Consumo (kWh)'].between(3, 4))]

"""**Ejemplo 5.25:**

Agrupar permite calcular estadísticas por categorías (como por fase o por hora).
"""

df.groupby('Fase')[['Voltaje (V)', 'Corriente (A)']].mean()

df.groupby('Fase').agg({
    'Voltaje (V)': ['mean', 'max'],
    'Corriente (A)': ['std'],
    'Consumo (kWh)': ['sum']
})

"""**Ejemplo 5.26:** Agrupar por hora

```python
df['Hora'] = df.index.hour
df.groupby('Hora')['Consumo (kWh)'].mean()
```
"""

df['Hora'] = df.index.hour
df.groupby('Hora')['Consumo (kWh)'].mean()

"""## Ejercicios

**Ejercicio 5.13:**

a. Agrega una columna `Energia_Aprox (Wh)` como `Consumo (kWh) * 1000`.
"""

# Espacio para resolver el ejercicio

"""b. Calcula la media móvil de 3 horas de consumo (`Consumo_3h`)."""

# Espacio para resolver el ejercicio

"""c. Usa `np.where()` para indicar si el consumo supera los 4 kWh."""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.14:**
Filtra las filas con THD > 6 y voltaje < 215.
"""

# Espacio para resolver el ejercicio
