# -*- coding: utf-8 -*-
"""

# Día 1 Parte 3: Instalación y Entorno de Desarrollo de Python

**Ejemplo 1.7: Definir Variables en un Circuito**
"""

# Variables de un circuito eléctrico
voltaje = 220  # Voltios
corriente = 5   # Amperios

# Imprimir valores
print(f"Voltaje: {voltaje} V")
print(f"Corriente: {corriente} A")

#O bien
print("Voltaje:", voltaje, "V")
print("Corriente:", corriente, "A")

"""Voltaje: 220 V
Corriente: 5 A
Voltaje: 220 V
Corriente: 5 A

**Ejemplo 1.8: Tipos de Datos en Componentes Eléctricos**
"""

resistencia = 50.5       # Ohmios (float)
nombre = "Motor"        # Nombre del componente (str)
estado = True            # ¿Está encendido? (bool)

# Imprimir tipos
print(type(resistencia))
print(type(nombre))
print(type(estado))

"""**Ejemplo 1.9: Cálculo de Potencia**"""

voltaje = 220
corriente = 5
potencia = voltaje * corriente  # Ley de Watt: P = V * I
print("Potencia:", potencia, "W")

"""**Ejemplo 1.10: Evaluar Seguridad en un Circuito**"""

temperatura = 85
corriente = 12

if temperatura > 80 and corriente > 10:
    print("  Advertencia: Riesgo de sobrecarga.")
else:
    print(" Circuito en condiciones seguras.")

"""**Ejemplo 1.11: Calculadora de Resistencia**"""

voltaje = float(input("Ingrese el voltaje (V): "))
corriente = float(input("Ingrese la corriente (A): "))

# Calcular resistencia
resistencia = voltaje / corriente

# Mostrar resultado
print(f"La resistencia es: {resistencia} Ohm")

"""**Ejemplo 1.12: Evaluación de Sobrecalentamiento en Transformadores**"""

# Evaluación de temperatura en un transformador
temperatura = float(input("Ingrese la temperatura del transformador (°C): "))

if temperatura > 80:
    print("  Advertencia: Temperatura crítica.")
elif temperatura > 60:
    print("  Temperatura elevada, pero dentro del rango seguro.")
else:
    print("  Temperatura normal.")

"""**Explicación:** - `input()` permite al usuario ingresar la temperatura. Se evalúan los rangos de temperatura para mostrar el estado del transformador.

**Ejemplo 1.12.1: Variación del ejemplo anterior - Añadir más niveles de alerta**
"""

# Evaluación de temperatura en un transformador
temperatura = float(input("Ingrese la temperatura del transformador (°C): "))
if temperatura > 90:
    print("¡Riesgo de incendio!")
elif temperatura > 80:
    print("Advertencia: Temperatura crítica.")
elif temperatura > 60:
    print("Temperatura elevada, pero dentro del rango seguro.")
else:
    print("Temperatura normal.")

"""## Ejercicios

**Ejercicio 1.5: Cree una lista de variables que describa un tablero eléctrico con 12 disyuntores.**
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 1.6:** Adapte el siguiente código para calcular la potencia cuando V=120, I=20; luego V=240, I=8; y finalmente V=34500, I=65."""

voltaje = 220
corriente = 5
potencia = voltaje * corriente  # Ley de Watt: P = V * I
print("Potencia:", potencia, "W")

# Espacio para solución del ejercicio.

"""**Ejercicio 1.7:** A partir del código del Ejemplo 1.12, crea un programa que evalúe si un transformador está en condiciones óptimas (`temperatura < 75` y `voltaje < 230`), a partir de estos valores definidos dentro del programa.

Nota: Dos condiciones en un condicional se pueden escribir:
* if temperatura < 75 and voltaje < 230:*
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 1.8:** Modifica el código para agregar una categoría
adicional: “Temperatura muy baja” si `temperatura < 40°C`.
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 1.9:** Detecte los errores y corrija el siguiente código:"""

temperatura = 80

if temperatura > 70:
    print("  Advertencia: Temperatura alta.")
if temperatura > 60:
    print("  Temperatura normal.")
if temperatura > 0:
    print("  Niveles normales.")

# Espacio para resolver el ejercicio
