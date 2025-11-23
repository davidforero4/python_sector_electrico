# -*- coding: utf-8 -*-
"""

# Sesión 2: Instalación y Entorno de Desarrollo de Python

**Ejemplo 1.5: Calculadora de Potencia**
"""

# Cálculo de potencia en un circuito eléctrico
def calcular_potencia(voltaje, corriente):
    """Calcula la potencia en vatios según la Ley de Ohm."""
    return voltaje * corriente

# Entrada de datos por el usuario
voltaje = float(input("Ingrese el voltaje (V): "))
corriente = float(input("Ingrese la corriente (A): "))

# Cálculo y salida de resultados
potencia = calcular_potencia(voltaje, corriente)
print(f"La potencia es: {potencia} W")

"""**Ejemplo 1.6 Gráfico de Consumo Energético**


"""

import matplotlib.pyplot as plt

# Datos de consumo por día
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
consumo = [120, 150, 130, 160, 140]

# Generación del gráfico
plt.plot(dias, consumo, marker='o', linestyle='-', color='b')
plt.title("Consumo Energético Semanal")
plt.xlabel("Día")
plt.ylabel("Consumo (kWh)")
plt.grid(True)
plt.show()
