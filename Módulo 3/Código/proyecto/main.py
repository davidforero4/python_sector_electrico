from paquete_electrico.circuitos import calcular_impedancia
from paquete_electrico.analisis.potencia import potencia_aparente

print(calcular_impedancia(10, 5))  # 11.18 ohm
print(potencia_aparente(220, 5))   # 1100 VA

