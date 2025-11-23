# -*- coding: utf-8 -*-
"""

Ejercicios de Corrección de Errores en Python
=============================================

A continuación, se presentan una serie de ejercicios diseñados para
identificar y corregir errores comunes en Python, especialmente
relevantes para aplicaciones en el sector eléctrico. Estos ejercicios
cubren problemas de sintaxis, indentación, tipos de datos y lógica
básica.

------------------------------------------------------------------------

Ejercicio 1.11: Error de Indentación en Cálculo de Potencia
----------------------------------------------------------

**Código con error:**

``` python
def calcular_potencia(voltaje, corriente):
potencia = voltaje * corriente  
return potencia

print(calcular_potencia(220, 10))
```

**Indicaciones:**
1. Identificar el error
2. Corregir el código
3. Explicar por qué es importante la indentación en Python
"""

# Espacio para resolver el ejercicio

"""Ejercicio 1.12: Error de Sintaxis en Ley de Ohm
----------------------------------------------

**Código con error:**

``` python
voltaje = 220
resistencia = 10
corriente = voltaje / resistencia

print("La corriente es:", corriente "A")  
```

**Indicaciones:**
1. Encontrar los dos errores de sintaxis
2. Corregir el código


"""

# Espacio para resolver el ejercicio

"""Ejercicio 1.13: Error de Tipo en Cálculo de Energía
--------------------------------------------------

**Código con error:**

``` python
potencia = "100"  # Definido como string
tiempo = 5
energia = potencia * tiempo  # Error: no se puede multiplicar string por int

print("Energía consumida:", energia, "kWh")
```

**Indicaciones:**
1. Identificar el error de tipos
2. Corregir el código
3. Explicar la diferencia entre tipos str e int


"""

# Espacio para resolver el ejercicio

"""Ejercicio 1.14: Error en Condicional de Temperatura
---------------------------------------------------

**Código con error:**

``` python
temperatura = 85

if temperatura > 80
    print("Advertencia: Alta temperatura")  # ¿dos puntos?
else
    print("Temperatura normal")  # ¿dos puntos?
```

**Indicaciones:**
1. Encontrar los dos errores de sintaxis
2. Corregir el código
3. Agregar una condición elif para temperatura >= 70


"""

# Espacio para resolver el ejercicio

"""Ejercicio 1.15: Error en Bucle While
------------------------------------

**Código con error:**

``` python
corriente = 5

while corriente < 15  
    print(f"Corriente: {corriente}A")
    corriente =+ 2  
```

**Indicaciones:**
1. Identificar los dos errores
2. Corregir el código


"""

# Espacio para resolver el ejercicio

# Solución
corriente = 5

while corriente < 15:  # Agregado dos puntos
    print(f"Corriente: {corriente}A")
    corriente += 2  # Corregido operador de incremento

"""Ejercicio 1.16: Error en Lista y For Loop
-----------------------------------------

**Código con error:**

``` python
voltajes = [220, 230, 210 240]  # ¿coma?

for v in voltajes
    print(f"Voltaje: {v}V")  # ¿dos puntos?
```

**Indicaciones:**
1. Encontrar los dos errores
2. Corregir el código



"""

# Espacio para resolver el ejercicio

"""Ejercicio Avanzado: Detección de Errores en Sistema de Monitoreo
----------------------------------------------------------------

**Código con múltiples errores:**

```
def monitorear_transformador(temperatura, corriente)
    if temperatura > 80 or corriente > 12
        estado = "Crítico"
    elif temperatura > 60 and corriente > 10
        estado = "Advertencia"
    else
        estado = "Normal"
    
    return estado

datos = [
    {"temp": 85, "corr": 10},
    {"temp": 70, "corr: 11},  # Falta comilla en "corr"
    {"temp": 50, "corr": 9}
]

for dato in datos
    print(monitorear_transformador(dato[temp], dato[corr]))  # Error en acceso a diccionario
```

**Indicaciones:**
1. Identificar y corregir los 5 errores
2. Explicar cada corrección

"""

# Espacio para resolver el ejercicio

"""**Solución:**

``` python
def monitorear_transformador(temperatura, corriente):
    if temperatura > 80 or corriente > 12:
        estado = "Crítico"
    elif temperatura > 60 and corriente > 10:
        estado = "Advertencia"
    else:
        estado = "Normal"
    
    return estado

datos = [
    {"temp": 85, "corr": 10},
    {"temp": 70, "corr": 11},  # Comilla agregada
    {"temp": 50, "corr": 9}
]

for dato in datos:
    print(f"Estado: {monitorear_transformador(dato['temp'], dato['corr'])}")  # Corregido acceso a diccionario
```

### Ejercicio: Detectar y corregir el error:

```
# Evaluación de temperatura en un transformador
temperatura = str(input("Ingrese la temperatura del transformador (°C): "))

if temperatura > 80:
    print("  Advertencia: Temperatura crítica.")
elif temperatura > 60:
    print("  Temperatura elevada, pero dentro del rango seguro.")
else:
    print("  Temperatura normal.")
```
"""

# Espacio para resolver el ejercicio

### **Ejercicio adicional: Análisis de Consumo**

Detecte y corrija el código del siguiente ejemplo

import matplotlib.pyplot as plt

# Datos de consumo en kWh
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
consumo = (10, 12, 8, 11)

plt.plot(dias, consumo, marker='o', linestyle='-', color='r')
plt.xlabel("Día")
plt.ylabel("Consumo (kWh)")
plt.title("Consumo Energético Semanal")
plt.grid(True)
plt.show()

# Espacio para resolver el ejercicio
