# -*- coding: utf-8 -*-
"""

# Día 1 Sesión 4: Bucles en Python


## Ejemplos

**Ejemplo 1.13: Monitoreo de Corriente con `while`**
"""

# Simulación de un sistema que monitorea la corriente
corriente = 5  # Amperios

while corriente <= 15:
    print(f"Corriente actual: {corriente} A")
    corriente += 2  # Incremento gradual en dos unidades

print("  Advertencia: Corriente crítica.")

Importante: Debemos tener cuidado con bucles infinitos:

# Simulación de un sistema que monitorea la corriente
corriente = 5  # Amperios

while corriente <= 15:
    print(f"Corriente actual: {corriente} A")

print("  Advertencia: Corriente crítica.")

"""**Ejemplo 1.14: Detener el bucle en un punto específico**:"""

corriente = 20  # Amperios
while corriente <= 20:
   if corriente == 12:
       print(" Advertencia: Corriente alcanzó 12 A, deteniendo monitoreo.")
       break
   print(f"Corriente actual: {corriente} A")
   corriente = corriente - 1

"""**Ejemplo 1.15: Cálculo de Potencia en Diferentes Corrientes**"""

# Potencia para diferentes valores de corriente
voltaje = 220
corrientes = [5, 10, 15, 20]

print("Corriente (A)\tPotencia (W)")
for corriente in corrientes:
    potencia = voltaje * corriente
    print(f"{corriente}\t\t{potencia}")

# Potencia para diferentes valores de corriente
voltaje = 220
corrientes = [5, 10, 15, 20]

print("Corriente (A)\tPotencia (W)")
for corriente in corrientes:
    potencia = voltaje * corriente
    print(f"{corriente}\t\t{potencia}")

"""En el ejemplo anterior, observe que `corriente` es variable, mientras que voltaje es una constante.

**Ejemplo 1.16 Variaciones del Ejemplo: Marcar con `sobrecarga` si la potencia supera los `3000 W`**
"""

# Potencia para diferentes valores de corriente
voltaje = 220
corrientes = [5, 10, 15, 20]
   for corriente in corrientes:
       potencia = voltaje * corriente
       if potencia > 3000:
           print(f"{corriente} A - {potencia} W   Sobrecarga")
       else:
           print(f"{corriente} A - {potencia} W")

# Potencia para diferentes valores de corriente
voltaje = 220
corrientes = [5, 10, 15, 20]
   for corriente in corrientes:
       potencia = voltaje * corriente
       if potencia > 3000:
           print(f"{corriente} A - {potencia} W   Sobrecarga")
       else:
           print(f"{corriente} A - {potencia} W")

"""## Ejercicios

**Ejercicio 1.10:**
Añade una condición para emitir una alerta si la corriente cae por debajo de `6 A`.
"""

# Espacio para resolver el ejercicio
