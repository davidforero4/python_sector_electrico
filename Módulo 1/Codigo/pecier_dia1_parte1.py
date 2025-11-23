# -*- coding: utf-8 -*-
"""

# Sesión 1: Introducción a Python

**Ejemplo 1.1: Filosofía de Python**
"""

import this

"""```
# Cálculo de la resistencia de un conductor según la Ley de Ohm
tension = 220  # en voltios
corriente = 10  # en amperios

resistencia = tension / corriente  # Ley de Ohm: R = V / I
print(f"La resistencia es {resistencia} ohmios")
```

Salida esperada:

```
La resistencia es 22.0 ohmios
```
La "f" significa que se está utilizando una cadena formateada (f-string). Otras posibilidades:

print("La resistencia es", resistencia, "ohmios")

print("El tiempo de operación es {} segundos".format(tiempo))

---

**Ejemplo 1.2: Variables**
"""

# Cálculo de la resistencia de un conductor según la Ley de Ohm
tension = 220  # en voltios
corriente = 10  # en amperios

resistencia = tension / corriente  # Ley de Ohm: R = V / I
print(f"La resistencia es {resistencia} ohmios")

"""---

**Ejemplo 1.3: Importancia de la indentación**
"""

voltaje=120
if voltaje > 0:
print("El voltaje es positivo")  # Esto generará un error de indentación

"""Corrección:"""

voltaje=120
if voltaje > 0:
    print("El voltaje es positivo")  # Correcto, con indentación adecuada

"""**Ejemplo 1.4: Mostrar tipos de variables.**"""

energia = 500.5  # Joules
potencia = 100  # Watts

tiempo = energia / potencia  # t = E / P
print(f"El tiempo de operación es {tiempo} segundos")

print(type(tiempo))

"""## Ejercicios

**Ejercicio 1.1:** Modificar el código del Ejemplo 1.2 para que la salida tenga el formato: "Dado una tensión de X voltios y una corriente de Y amperios, sabemos que la resistencia tiene un valor de Z ohmios."
"""

# Espacio para solución del ejercicio.

"""---

**Ejercicio 1.2:** Modificar el Ejemplo 1.3 para contemplar los casos de voltaje negativo o cero.
"""

# Espacio para resolver el ejercicio

"""---

**Ejercicio 1.3:** Modificar el Ejemplo 1.4 para verificar el tipo de datos de la variable tiempo, si energia=500
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 1.4:** Detectar y corregir los errores en el siguiente código:"""

energia = 500.5  # Joules
potencia = 100  # Watts

tiempo = energia / potencia  # t = E / P

if tiempo >= 0:
print(f"El valor de tiempo es: tiempo")

# Espacio para resolver el ejercicio
