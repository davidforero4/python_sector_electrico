# -*- coding: utf-8 -*-
"""PECIER_dia2_parte1.ipynb

# Día 2 Parte 1: Introducción a las Estructuras de Datos

**Ejemplo 2.1**: Listas
"""

# Crear una lista de valores de corriente
corrientes = [5, 10, 15, 20]

# Acceder a elementos
print("Primera corriente:", corrientes[0])
print("Última corriente:", corrientes[-1])

"""**Salida esperada**:
Primera corriente: 5
Última corriente: 20

Importante: Observemos la forma en que se indexan los elementos de la lista.

**Ejemplo 2.2**:
"""

corrientes = [5, 10, 15, 20]
# Modificar un elemento
corrientes[1] = 12
print("Lista modificada:", corrientes)

# Agregar un elemento
corrientes.append(25)
print("Lista con nuevo elemento:", corrientes)

"""**Salida esperada**:
Lista modificada: [5, 12, 15, 20]
Lista con nuevo elemento: [5, 12, 15, 20, 25]

**Ejemplo 2.2.1:**
"""

# Crear una lista de valores de corriente
corrientes = [5, 10, 15, 20]

# Eliminar elementos
corrientes.pop(0) # Elimina el primer elemento
print("Nueva lista:", corrientes)

"""**Ejemplo 2.3**:"""

# Ordenar la lista de corrientes
# Crear una lista de valores de corriente
corrientes = [5, 10, 1, 20]
corrientes.sort()
print("Lista ordenada:", corrientes)

# También se puede considerar:
corrientes.sort(reverse=True)
print("Lista ordenada en orden inverso:", corrientes)

# Eliminar un elemento
# Eliminar el elemento en el índice 2 (el valor 15)
corrientes.pop(2)
print("Lista después de eliminar el índice 2:", corrientes)

"""**Ejemplo 2.4**: Tuplas"""

# Crear una tupla de valores de temperatura
temperaturas = (75, 80, 85, 90)

# Acceder a elementos
print("Primera temperatura:", temperaturas[0])
print("Última temperatura:", temperaturas[-1])

"""**Salida esperada**:

Primera temperatura: 75
Última temperatura: 90

**Ejemplo 2.5**:
"""

# Intentar modificar una tupla (generará un error)
# Crear una tupla de valores de temperatura
temperaturas = (75, 80, 85, 90)

temperaturas[1] = 82

# Ejemplo de concatenación
a = (1, 2)
b = (3, 4)
c = a + b
print(c)  # (1, 2, 3, 4)

# Ejemplo de extraer partes:
t = (1, 2, 3, 4, 5)
print(t[1:4])  # (2, 3, 4)

"""**Ejemplo 2.6**: Diccionarios"""

componentes = {
    "resistencia": "10 Ohm",
    "capacitor": "100 uF",
    "inductor": "50 mH"
}

# Acceder a un valor
print("Valor del capacitor:", componentes["capacitor"])

"""**Salida esperada**:
Valor del capacitor: 100 µF

**Ejemplo 2.7:**
"""

# Crear un diccionario de componentes eléctricos
componentes = {
    "resistencia": "10 Ω",
    "capacitor": "100 µF",
    "inductor": "50 mH"
}

# Agregar un nuevo componente
componentes["diodo"] = "1N4007"
print("Diccionario actualizado:", componentes)

# Modificar un valor
componentes["resistencia"] = "20 Ω"
print("Diccionario modificado:", componentes)

"""**Ejemplo 2.8**: Conjunto"""

# Crear un conjunto de valores de corriente
corrientes = {5, 10, 15, 20}

# Agregar un elemento
corrientes.add(25)
print("Conjunto con nuevo elemento:", corrientes)

# Eliminar un elemento
corrientes.remove(10)
print("Conjunto sin el 10:", corrientes)

"""**Ejemplo 2.9**:"""

# Operaciones con conjuntos
conjunto1 = {5, 10, 15}
conjunto2 = {10, 15, 20}

print("Unión:", conjunto1.union(conjunto2))
print("Intersección:", conjunto1.intersection(conjunto2))

"""**Salida esperada**:
Unión: {5, 10, 15, 20}
Intersección: {10, 15}

**Ejemplo 2.10:**:
"""

# Conjunto de valores de corriente
corrientes = {5, 10, 15, 20}

# Convertir a lista
lista_corrientes = list(corrientes)

print("Tipo:", type(lista_corrientes))  # <class 'list'>
print("Lista:", lista_corrientes)

"""## Ejercicios

**Ejercicio 2.1**: Verificar si una lista permite variables heterogéneas (como int y float)
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 2.2**: Crea una lista con valores de tensiones , a partir del Ejemplo 1.1 (por ejemplo, `[220, 221, 218]`) y mostrar el segundo valor.


"""

# Espacio para resolver el ejercicio

"""**Ejercicio 2.3**: Ordene la lista de voltajes y elimine el valor más bajo. Sugerencia: Combine los ejemplos 2.2.1 y 2.3

"""

# Espacio para resolver el ejercicio.

"""**Ejercicio 2.5**: Ordene la lista de voltajes y elimine el valor más alto."""

# Espacio para resolver el ejercicio.

"""**Ejercicio 2.6**: Crear una tupla con diez valores de resistencia (por ejemplo, `(10, 20, 30, ..., 100)`) y muestra el tercer valor.

"""

# Espacio para resolver el ejercicio.

"""**Ejercicio 2.7**:
Crear un conjunto con valores de temperatura (por ejemplo, `{75, 80, 85}`) y agrega un nuevo valor de 90.
"""

# Espacio para resolver el ejercicio

"""**Ejercicio 2.8:** Lista de Voltajes  - Identifique el error y corríjalo en los siguientes ejemplos:

"""

# Crear una lista de voltajes
voltajes = [220, 110, 440]

# Ordenar y mostrar el valor más alto
voltajes.sort()
print("Voltaje más alto:", voltajes[3])

"""**Corrección:**"""

# Espacio para resolver el ejercicio

"""
**Ejercicio 2.10: Diccionario de Componentes — Identifique el error y corríjalo en los siguientes ejemplos:**"""

# Crear un diccionario de componentes
componentes = {
    "resistencia": "10 Ω",
    "capacitor": "100 µF",
    "inductor": "50 mH"
}

# Agregar y modificar componentes
componentes[diodo] = "1N4007"
componentes[resistencia] = "20 Ω"

# Mostrar el diccionario actualizado
print("Diccionario actualizado:", componentes)

"""**Corrección:**"""

# Espacio para resolver el ejercicio

# Sugerencias para el anterior:
componentes["diodo"] = "1N4007"
componentes["resistencia"] = "20 Ω"

"""**Ejercicio 2.11: Sin ejecutar el código, cuál es el valor de la salida del siguiente código**

```
# Crear una lista de valores de corriente
corrientes = [0, 10, 15, 5, 3]

# Acceder a elementos
print("Corriente:", corrientes[1])
```
"""

# Espacio para verificación:

"""**Ejercicio 2.12: Sin ejecutar el código, cuál es el valor de la salida del siguiente código**

```
# Crear una lista de valores de corriente
corrientes = [1, 3, 5, 2]

# Acceder a elementos
print("Corriente:", corrientes[-2])
```
"""

# Espacio para verificación:
