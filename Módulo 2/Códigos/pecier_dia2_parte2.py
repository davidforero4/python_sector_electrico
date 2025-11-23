# -*- coding: utf-8 -*-
"""PECIER_dia2_parte2.ipynb

# Día 2 Parte 2: Bucles Anidados y Control de Flujo Avanzado
"""

# Configuración inicial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Bibliotecas cargadas correctamente!")

"""## Ejemplos

**Ejemplo 2.11:**
"""

# Matriz de covarianzas
cov = [
    [0.75, 0.78, 0.80],
    [0.77, 0.82, 0.79],
    [0.85, 0.88, 0.90]
]

for i, fila in enumerate(cov):
    for j, co in enumerate(fila):
        if co > 0.85:
            print(f" Alerta en posición ({i},{j}): {co}")
        else:
            print(f"Posición ({i},{j}): {co} normal")

"""Importante: La función enumerate devuelve dos valores: el índice de la fila (i) y la fila misma (fila). Por esto es que se utilizan dos variables en el for.

"""

# Matriz de covarianzas
cov = [
    [0.75, 0.78, 0.80],
    [0.77, 0.82, 0.79],
    [0.85, 0.88, 0.90]
]

for i, fila in enumerate(cov):
    for j, co in enumerate(fila):
        if co > 0.85:
            print(f" Alerta en posición ({i},{j}): {co}")
        else:
            print(f"Posición ({i},{j}): {co} normal")

"""**Ejercicio 2.12**

Detecte el error y corrija el siguiente código:
"""

# Matriz de covarianzas
cov = [
    [0.75, 0.78, 0.80],
    [0.77, 0.82, 0.79],
    [0.85, 0.88, 0.90]
]

for i, fila in enumerate(cov):
    for j, co in enumerate(fila):
        if co > 0.85:
            print(f" Alerta en posición ({i},{j}): {co}")
        else:
            print(f"Posición ({i},{j}): {temp} normal")

# Espacio para resolver el ejercicio

"""
**Ejemplo 2.13: Análisis de Circuitos Paralelos**  
Este código está diseñado para calcular todas las combinaciones posibles de tres resistencias conectadas en paralelo y su resistencia equivalente. Las combinaciones se extraen de una lista de  valores predefinidos de resistencias y se evita la repetición de combinaciones mediante la condición r1 < r2 < r3.

"""

# Definir una lista con los valores de resistencia en ohmios (Ohm)
resistencia_valores = [10, 20, 30, 40, 50]

# Lista vacía para almacenar las combinaciones de resistencias y sus respectivas resistencias equivalentes
combinaciones = []

# Iniciar un bucle anidado para iterar sobre las 3 resistencias (r1, r2, r3)
# Esto para probar todas las combinaciones posibles de resistencias
# utilizando los valores disponibles en la lista 'resistencia_valores'
for r1 in resistencia_valores:          # Primer bucle: itera sobre r1
    for r2 in resistencia_valores:      # Segundo bucle: itera sobre r2
        for r3 in resistencia_valores:  # Tercer bucle: itera sobre r3
            # Asegurar que las combinaciones no se repitan, es decir, r1 debe ser menor que r2, y r2 menor que r3
            if r1 < r2 < r3:
                # Fórmula para la resistencia equivalente en paralelo:
                # 1/R_eq = 1/R1 + 1/R2 + 1/R3
                r_eq = 1 / (1/r1 + 1/r2 + 1/r3)  # Calcular la resistencia equivalente
                # Almacenar las resistencias y la resistencia equivalente en la lista 'combinaciones'
                combinaciones.append([r1, r2, r3, round(r_eq, 2)])

# Imprimir las combinaciones de resistencias y su resistencia equivalente
# Mostrar solo las primeras 5 combinaciones (para evitar imprimir demasiado texto)
for comb in combinaciones[:5]:
    print(f"Resistencias: R1 = {comb[0]} Ohm, R2 = {comb[1]} Ohm, R3 = {comb[2]} Ohm -> R_Equiv = {comb[3]} Ohm")

# Imprimir todas las combinaciones
# for comb in combinaciones:
#     print(f"Resistencias: R1 = {comb[0]} Ohm, R2 = {comb[1]} Ohm, R3 = {comb[2]} Ohm -> R_Equiv = {comb[3]} Ohm")

"""**Ejemplo 2.14: Uso de `break`**  """

# Sistema de detección de fallas en tiempo real
lecturas = [5, 8, 15, 18, 12, 25, 9]  # Corrientes en A
umbral_critico = 20

for i, corriente in enumerate(lecturas, 1):
    print(f"Lectura {i}: {corriente}A")
    if corriente > umbral_critico:
        print(f"¡Falla detectada! Corte de emergencia en lectura {i}")
        break
else:
    print("Sistema operando normalmente")

"""El break hace que el bucle se detenga de inmediato, interrumpiendo cualquier procesamiento adicional, ya que ya se ha detectado una situación crítica.

## Ejercicios

**Ejercicio 2.13:**
A partir de código del **Ejemplo 2.13** , responda las siguientes preguntas:

1. ¿Cuál es el efecto de eliminar la condición `r1<r2<r3`?

2. ¿Cuántas combinaciones existen para 8 resistencias?
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 2.14: A partir de código del ejemplo 2.14, responder las siguientes preguntas:**

- ¿La instrucción break detiene todo el programa o solamente el bucle?


"""

# Espacio para resolver el ejercicio

"""**Ejercicio 2.15: Analice y corrija el error en el siguiente código.**"""

import time # Esta línea la analizaremos posteriormente:

# Sistema de detección de fallas en tiempo real con temporizador
lecturas = [5, 8, 15, 18, 12, 25, 9]  # Corrientes en A
umbral_critico = 20;
tiempo_total = 0  # Inicializamos el tiempo total en segundos

for i, corriente in enumerate(lecturas, 1):
    print(f"Lectura {i}: {corriente}A")
    tiempo_total += 1  # Sumar 1 segundo por cada lectura
    time.sleep(1)  # Simular un retraso de 1 segundo por lectura

    if corriente > umbral_critico:
        print(f"¡Falla detectada! Corte de emergencia en lectura {i}")
        break
else:
print("Sistema operando normalmente")

# Mostrar el tiempo total de monitoreo
print(f"Tiempo total de monitoreo: {tiempo_total} segundos")

"""**Corrección:**"""

# Espacio para resolver el ejercicio:

"""
**Ejercicio 2.16:** Ejecutar el siguiente código y explicar el resultado:
"""

# Filtrar mediciones válidas de voltaje
datos_crudos = [218, -1, 225, 999, 230, 0, 235]  # -1 y 999 son errores
datos_validos = []

for voltaje in datos_crudos:
    if voltaje < 200 or voltaje > 250:
        print(f"Descartado: {voltaje}V (fuera de rango)")
        continue
    datos_validos.append(voltaje)

print("\nDatos válidos para análisis:", datos_validos)

# Espacio para resolver el ejercicio:

"""## **Proyecto Integrador**  
### **Sistema de Monitoreo Inteligente**  
**Objetivo:** Desarrollar un programa que:
1. Simule lecturas de múltiples sensores (temperatura, corriente, voltaje)
2. Detecte anomalías usando bucles anidados
3. Genere reportes automatizados
"""

# Ejemplo de solución.
import numpy as np

# Simulación de datos de sensores
n_sensores = 3  # Número de sensores
n_lecturas = 5  # Número de lecturas por sensor
datos = np.random.rand(n_sensores, n_lecturas) * 100  # Datos aleatorios (simulando sensores)

# Mostrar los datos simulados
print("Datos simulados:")
print(datos)

# Análisis de datos (detección de anomalías)
reporte = []  # Lista para almacenar los reportes de anomalías
for i, sensor in enumerate(datos):  # Iterar sobre cada sensor
    for j, valor in enumerate(sensor):  # Iterar sobre cada lectura del sensor
        if valor > 85:  # Definir umbral de anomalía
            reporte.append(f"Sensor {i+1}, Lectura {j+1}: CRÍTICO ({valor:.2f})")

# Mostrar los resultados del análisis
print("\nAnálisis de anomalías:")
if reporte:  # Si hay anomalías reportadas
    print(*reporte, sep='\n')
else:
    print("No se detectaron anomalías.")

# Espacio para solucion

"""**Preguntas:**
1. Determinar por qué se usa un * en print(*reporte). Puede realizar la prueba en el siguiente código:


```python
# Ejemplo de solución.
import numpy as np

# Simulación de datos de sensores
n_sensores = 3  # Número de sensores
n_lecturas = 5  # Número de lecturas por sensor
datos = np.random.rand(n_sensores, n_lecturas) * 100  # Datos aleatorios (simulando sensores)

# Mostrar los datos simulados
print("Datos simulados:")
print(datos)

# Análisis de datos (detección de anomalías)
reporte = []  # Lista para almacenar los reportes de anomalías
for i, sensor in enumerate(datos):  # Iterar sobre cada sensor
    for j, valor in enumerate(sensor):  # Iterar sobre cada lectura del sensor
        if valor > 85:  # Definir umbral de anomalía
            reporte.append(f"Sensor {i+1}, Lectura {j+1}: CRÍTICO ({valor:.2f})")

# Mostrar los resultados del análisis
print("\nAnálisis de anomalías:")
if reporte:  # Si hay anomalías reportadas
    print(*reporte, sep='\n')
else:
    print("No se detectaron anomalías.")

```

"""



"""
## **5. Ejercicio Adicional**  
### **Optimización de Configuraciones**  

1. Analice el siguiente código, encuentre y corrija los errores presentes.

```
# Encontrar la combinación de resistencias que más se aproxime a un valor deseado
# Definir una lista con los valores de resistencia en ohmios (Ohm)
resistencia_valores = [10, 20, 30, 40, 50]

# Lista vacía para almacenar las combinaciones de resistencias y sus respectivas resistencias equivalentes
combinaciones = []

# Valor objetivo que el usuario quiere aproximar
valor_objetivo = float(input("Introduce el valor objetivo de resistencia (Ohm): "))

# Iniciar un bucle anidado para iterar sobre las 3 resistencias (r1, r2, r3)
# Estos bucles anidados permiten probar todas las combinaciones posibles de resistencias
# utilizando los valores disponibles en la lista 'resistencia_valores'
for r1 in resistencia_valores:          # Primer bucle: itera sobre r1
    for r2 in resistencia_valores:      # Segundo bucle: itera sobre r2
        for r3 in resistencia_valores:  # Tercer bucle: itera sobre r3
            # Asegurar que las combinaciones no se repitan, es decir, r1 debe ser menor que r2, y r2 menor que r3
            if r1 < r2 < r3:
                # Fórmula para la resistencia equivalente en paralelo:
                # 1/R_eq = 1/R1 + 1/R2 + 1/R3
                r_eq = 1 / (1/r1 + 1/r2 + 1/r3)  # Calcular la resistencia equivalente
                # Almacenar las resistencias y la resistencia equivalente en la lista 'combinaciones'
                combinaciones.append([r1, r2, r3, round(r_eq, 2)])

# Encontrar la combinación cuya resistencia equivalente sea la más cercana al valor objetivo
mejor_combinacion = None
diferencia_minima = float('inf')  # Inicializamos con un valor muy grande para la diferencia

for comb in combinaciones:
    r_eq = comb[3]
    # Calcular la diferencia absoluta entre la resistencia equivalente y el valor objetivo
    diferencia = abs(r_eq - valor_objetivo)
    
    # Si esta diferencia es menor que la mínima encontrada hasta ahora, actualizamos
    if diferencia < diferencia_minima:
    diferencia_minima = diferencia
    mejor_combinacion = comb

# Imprimir las primeras 5 combinaciones de resistencias y su resistencia equivalente
print("\nLas primeras 5 combinaciones de resistencias son:")
for comb in combinaciones[:5]:
    print(f"Resistencias: R1 = {comb[0]} Ohm, R2 = {comb[1]} Ohm, R3 = {comb[2]} Ohm -> R_Equiv = {comb[3]} Ohm")

# Imprimir la mejor combinación encontrada
if mejor_combinacion:
    print(f"\nLa combinación más cercana al valor objetivo ({valor_objetivo} Ohm) es:")
    print(f"Resistencias: R1 = {mejor_combinacion[1]} Ohm, R2 = {mejor_combinacion[2]} Ohm, R3 = {mejor_combinacion[3]} Ohm -> R_Equiv = {mejor_combinacion[3]} Ohm")

```
"""

# Encontrar la combinación de resistencias que más se aproxime a un valor deseado
# Definir una lista con los valores de resistencia en ohmios (Ohm)
resistencia_valores = [10, 20, 30, 40, 50]

# Lista vacía para almacenar las combinaciones de resistencias y sus respectivas resistencias equivalentes
combinaciones = []

# Valor objetivo que el usuario quiere aproximar
valor_objetivo = float(input("Introduce el valor objetivo de resistencia (Ohm): "))

# Iniciar un bucle anidado para iterar sobre las 3 resistencias (r1, r2, r3)
# Estos bucles anidados permiten probar todas las combinaciones posibles de resistencias
# utilizando los valores disponibles en la lista 'resistencia_valores'
for r1 in resistencia_valores:          # Primer bucle: itera sobre r1
    for r2 in resistencia_valores:      # Segundo bucle: itera sobre r2
        for r3 in resistencia_valores:  # Tercer bucle: itera sobre r3
            # Asegurar que las combinaciones no se repitan, es decir, r1 debe ser menor que r2, y r2 menor que r3
            if r1 < r2 < r3:
                # Fórmula para la resistencia equivalente en paralelo:
                # 1/R_eq = 1/R1 + 1/R2 + 1/R3
                r_eq = 1 / (1/r1 + 1/r2 + 1/r3)  # Calcular la resistencia equivalente
                # Almacenar las resistencias y la resistencia equivalente en la lista 'combinaciones'
                combinaciones.append([r1, r2, r3, round(r_eq, 2)])

# Encontrar la combinación cuya resistencia equivalente sea la más cercana al valor objetivo
mejor_combinacion = None
diferencia_minima = float('inf')  # Inicializamos con un valor muy grande para la diferencia

for comb in combinaciones:
    r_eq = comb[3]
    # Calcular la diferencia absoluta entre la resistencia equivalente y el valor objetivo
    diferencia = abs(r_eq - valor_objetivo)

    # Si esta diferencia es menor que la mínima encontrada hasta ahora, actualizamos
    if diferencia < diferencia_minima:
    diferencia_minima = diferencia
    mejor_combinacion = comb

# Imprimir las primeras 5 combinaciones de resistencias y su resistencia equivalente
print("\nLas primeras 5 combinaciones de resistencias son:")
for comb in combinaciones[:5]:
    print(f"Resistencias: R1 = {comb[0]} Ohm, R2 = {comb[1]} Ohm, R3 = {comb[2]} Ohm -> R_Equiv = {comb[3]} Ohm")

# Imprimir la mejor combinación encontrada
if mejor_combinacion:
    print(f"\nLa combinación más cercana al valor objetivo ({valor_objetivo} Ohm) es:")
    print(f"Resistencias: R1 = {mejor_combinacion[1]} Ohm, R2 = {mejor_combinacion[2]} Ohm, R3 = {mejor_combinacion[3]} Ohm -> R_Equiv = {mejor_combinacion[3]} Ohm")
