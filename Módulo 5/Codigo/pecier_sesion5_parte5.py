# -*- coding: utf-8 -*-
"""

# Día 5 Parte 5: Visualización de Datos con Matplotlib y Seaborn para aplicaciones del Sector Eléctrico

## Ejemplos

**Ejemplo 5.27:** Cargar bibliotecas y crear dataset de ejemplo
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.style.use('seaborn-v0_8')  # Estilo predeterminado moderno
sns.set_palette("husl")        # Paleta de colores para Seaborn
# %matplotlib inline

"""**Ejemplo 5.28:** Crear datos de simulación"""

np.random.seed(42)

horas = pd.date_range('2023-06-01', periods=24, freq='H')
datos = {
    'Hora': horas,
    'Voltaje': np.random.normal(220, 5, 24),
    'Corriente': np.random.gamma(5, 0.5, 24),
    'Potencia': np.random.uniform(1000, 5000, 24),
    'Fase': np.random.choice(['R', 'S', 'T'], 24)
}
df = pd.DataFrame(datos).set_index('Hora')

"""**Ejemplo 5.29:** Voltaje a lo largo del día"""

plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Voltaje'],
         marker='o',            # Estilo del punto (otros: 's' cuadrado, '^' triángulo)
         linestyle='--',        # '--' = línea punteada. También: '-' sólida, '-.', ':'
         color='b',             # 'b' = azul. Otros: 'r' rojo, 'g' verde, 'k' negro
         label='Voltaje (V)')   # Etiqueta de leyenda

plt.axhline(220, color='r', linestyle=':', label='Valor nominal')
plt.title('Variación de Voltaje en 24 Horas')
plt.xlabel('Hora del día')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()

"""#### Explicación de cada línea

| Elemento         | Significado                            |
|-- | -- |
| `plt.plot()`     | Crea gráfico de líneas                 |
| `marker='o'`     | Marca cada punto con círculo           |
| `linestyle='--'` | Línea punteada                         |
| `color='b'`      | Color azul                             |
| `axhline()`      | Línea horizontal (valor de referencia) |

**Ejemplo 5.30:** Distribución de corriente
"""

plt.figure(figsize=(10, 6))
plt.hist(df['Corriente'],
         bins=8,                # Número de bloques
         color='green',
         alpha=0.7,             # Transparencia (0 = invisible, 1 = opaco)
         edgecolor='black')     # Borde de las barras
plt.title('Distribución de Corriente')
plt.xlabel('Corriente (A)')
plt.ylabel('Frecuencia')
plt.show()

"""**Ejemplo 5.31:**"""

plt.figure(figsize=(10, 6))
plt.scatter(df['Corriente'], df['Potencia'],
            c=pd.factorize(df['Fase'])[0], # Codifica R/S/T como 0/1/2
            cmap='viridis',                # Mapa de color
            s=100)                         # Tamaño de puntos
plt.colorbar(label='Fase')
plt.plot(np.unique(df['Corriente']),
         np.poly1d(np.polyfit(df['Corriente'], df['Potencia'], 1))(np.unique(df['Corriente'])),
         'r--')  # Línea de regresión (roja punteada)
plt.title('Relación Corriente-Potencia')
plt.xlabel('Corriente (A)')
plt.ylabel('Potencia (W)')
plt.show()

"""**Ejemplo 5.32:**"""

plt.figure(figsize=(10, 6))
#sns.boxplot(x='Fase', y='Voltaje', data=df.reset_index(),
#            width=0.3, notch=True)  # notch=True muestra intervalo de confianza
sns.swarmplot(x='Fase', y='Voltaje', data=df.reset_index(),
              color='black', alpha=0.5)  # Puntos individuales
plt.title('Distribución de Voltaje por Fase')
plt.show()

"""Recomendación: Ver https://www.geeksforgeeks.org/python/swarmplot-using-seaborn-in-python/

**Ejemplo 5.33:**
"""

corr = df[['Voltaje', 'Corriente', 'Potencia']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.title('Matriz de Correlación')
plt.show()

"""**Ejemplo 5.34:**
Este gráfico muestra cómo varía el voltaje cada día, comparando por hora.
"""

semana = pd.date_range('2023-06-01', periods=7*24, freq='H')
df_semana = pd.DataFrame({
    'Timestamp': semana,
    'Voltaje': np.random.normal(220, 3, len(semana)) + 5*np.sin(2*np.pi*semana.hour/24),
    'Consumo': np.random.gamma(5, 100, len(semana)),
    'Dia': semana.day_name(),
    'Hora': semana.hour
}).set_index('Timestamp')

plt.figure(figsize=(14, 7))
sns.lineplot(data=df_semana.reset_index(),
             x='Hora',
             y='Voltaje',
             hue='Dia',
             style='Dia',
             markers=True,
             dashes=False,
             palette='tab10')
plt.title('Variación Diaria de Voltaje durante una Semana')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

"""**Ejemplo 5.35: Dashboard**

Vamos a construir un dashboard que incluya:

* Serie temporal
* Histograma
* Boxplot
* Mapa de calor
* Dispersión con colores por día
"""

def crear_dashboard(df):
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 2)

    # Gráfico 1: Voltaje en el tiempo
    ax1 = fig.add_subplot(gs[0, :])
    sns.lineplot(data=df.reset_index(),
                 x='Timestamp',
                 y='Voltaje',
                 ax=ax1)
    ax1.set_title('Voltaje en el Tiempo')
    ax1.set_ylabel('Voltaje (V)')
    ax1.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m %H:%M'))

    # Gráfico 2: Histograma de consumo
    ax2 = fig.add_subplot(gs[1, 0])
    sns.histplot(data=df,
                 x='Consumo',
                 bins=15,
                 kde=True,  # Curva de densidad
                 ax=ax2)
    ax2.set_title('Distribución de Consumo')

    # Gráfico 3: Boxplot de voltaje por hora
    ax3 = fig.add_subplot(gs[1, 1])
    sns.boxplot(data=df.reset_index(),
                x='Hora',
                y='Voltaje',
                ax=ax3)
    ax3.set_title('Voltaje por Hora del Día')

    # Gráfico 4: Mapa de calor de consumo por día/hora
    ax4 = fig.add_subplot(gs[2, 0])
    pivot = df.reset_index().pivot_table(values='Consumo',
                                         index='Hora',
                                         columns='Dia')
    sns.heatmap(pivot,
                cmap='YlOrRd',
                annot=True,
                fmt='.0f',
                ax=ax4)
    ax4.set_title('Consumo por Hora y Día')

    # Gráfico 5: Dispersión voltaje-consumo
    ax5 = fig.add_subplot(gs[2, 1])
    sns.scatterplot(data=df.reset_index(),
                    x='Voltaje',
                    y='Consumo',
                    hue='Dia',
                    palette='viridis',
                    ax=ax5)
    ax5.set_title('Relación Voltaje-Consumo')

    plt.tight_layout()
    plt.savefig('dashboard_electrico.png', dpi=300)
    plt.show()

crear_dashboard(df_semana)

"""### Explicación

* Se usa `gridspec` para organizar el layout (3 filas × 2 columnas)
* Cada gráfico ocupa su propia celda o combinación de celdas
* Las visualizaciones permiten inspección cruzada de variable

**Ejercicio 5.36 Detección con 2 desviaciones estándar**
"""

def detectar_anomalias(df):
    mean_v = df['Voltaje'].mean()
    std_v = df['Voltaje'].std()

    df['Anomalia'] = (df['Voltaje'] < mean_v - 2 * std_v) | \
                     (df['Voltaje'] > mean_v + 2 * std_v)

    plt.figure(figsize=(14, 6))
    sns.scatterplot(data=df.reset_index(),
                    x='Timestamp',
                    y='Voltaje',
                    hue='Anomalia',
                    palette={True: 'red', False: 'blue'},
                    style='Anomalia',
                    s=100)
    plt.axhline(mean_v, color='green', linestyle='--', label='Media')
    plt.axhline(mean_v + 2 * std_v, color='orange', linestyle=':', label='Límites')
    plt.axhline(mean_v - 2 * std_v, color='orange', linestyle=':')
    plt.title('Detección de Anomalías en Voltaje')
    plt.legend()
    plt.show()

    return df[df['Anomalia']]

anomalias = detectar_anomalias(df_semana)
print(f"Anomalías detectadas: {len(anomalias)}")

"""## Ejercicios

**Ejercicio 5.15:**

Modifica el gráfico del ejercicio 5.18 para:

1. Cambiar la línea a estilo sólido (`linestyle='-'`)
"""

# Espacio para resolver el ejercicio

2. Usar color verde para el voltaje

# Espacio para resolver el ejercicio

"""3. Añadir línea horizontal a 230 V"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.16:**

1. Aumenta los bins a 12 del ejemplo 5.19
"""

# Espacio para resolver el ejercicio

"""2. Cambia el color a naranja"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.17:**

1. Usar `s=50` para puntos más pequeños usando de ejemplo el código del ejemplo 5.20
"""

# Espacio para resolver el ejercicio

"""2. Cambiar `cmap` a `'plasma'`"""

# Espacio para resolver el ejercicio

"""3. Eliminar la línea de regresión"""

# Espacio para resolver el ejercicio

"""**Ejercicio 5.18:**

1. Usar `cmap='YlGnBu'`
"""

# Espacio para resolver el ejercicio

2. Quitar las líneas (`linewidths=0`)

# Espacio para resolver el ejercicio

"""**Ejercicio 5.19:**

1. Desactivar los `markers` Mostrados en el ejemplo 5.24
"""

# Espacio para resolver el ejercicio

"""2. Cambiar `palette` a `'Set2'`"""

# Espacio para resolver el ejercicio

# Extra: Incluir promedio por hora
promedio_por_hora = df_semana.groupby('Hora')['Voltaje'].mean().reset_index()
promedio_por_hora['Dia'] = 'Promedio'  # etiqueta para distinguirlo

# Preparar datos para graficar: concatenar el promedio con los datos originales
df_grafico = pd.concat([df_semana.reset_index(), promedio_por_hora], ignore_index=True)

plt.figure(figsize=(14, 7))
sns.lineplot(data=df_grafico.reset_index(),
             x='Hora',
             y='Voltaje',
             hue='Dia',
             style='Dia',
             markers=True,
             dashes=False,
             palette='tab10')
plt.title('Variación Diaria de Voltaje durante una Semana')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

"""**Ejercicios 5.20:**

1. Con base al ejemplo 5.36: Usa 1.5 desviaciones estándar en lugar de 2
"""

# Espacio para resolver el ejercicio

"""2. Marcar anomalías con un triángulo rojo"""

# Espacio para resolver el ejercicio
