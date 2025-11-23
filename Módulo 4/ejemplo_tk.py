# Fuente: https://tkdocs.com/tutorial/firstexample.html

from tkinter import *
from tkinter import ttk

# Función que convierte pies a metros
def calcular(*args):
    # Obtener el valor introducido en el campo de texto 'feet'
    valor = feet.get()

    # Verificar si el valor introducido es un número válido
    if valor.replace('.', '', 1).isdigit():
        # Si es un número válido, convertir los pies a metros y mostrar el resultado
        metros.set(round(0.3048 * float(valor), 4))
    else:
        # Si no es un número válido, mostrar un mensaje de error
        metros.set("¡Error! No se introdujo un número válido.")

# Crear la ventana principal de la aplicación
root = Tk()

# Asignar un título a la ventana
root.title("Conversión de Pies a Metros")

# Crear un marco dentro de la ventana principal para contener los widgets
# Un "widget" es un componente de la interfaz gráfica de usuario, como botones, campos de texto, etiquetas, etc.
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Variable que guarda el valor introducido en el campo de texto para los pies
feet = StringVar()

# Crear un campo de texto (entrada) donde el usuario puede escribir el valor en pies
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Variable que guardará el resultado de la conversión a metros
metros = StringVar()

# Crear una etiqueta para mostrar el resultado de la conversión (en metros)
ttk.Label(mainframe, textvariable=metros).grid(column=2, row=2, sticky=(W, E))

# Crear un botón que cuando se presione, ejecute la función 'calcular'
ttk.Button(mainframe, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W)

# Etiquetas que sirven para describir los campos de entrada y salida
ttk.Label(mainframe, text="pies").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="equivalen a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

# Configuración para que la ventana se ajuste al tamaño de su contenido
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

# Ajustar el espacio entre los widgets para que no se vean amontonados
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Establecer el foco (cursor) en el campo de texto de 'pies' cuando se abre la aplicación
feet_entry.focus()

# La función bind conecta la tecla 'Enter' con la acción de calcular
# Esto significa que si presionamos "Enter", se ejecutará la función 'calcular'
root.bind("<Return>", calcular)

# El método mainloop inicia la aplicación y mantiene la ventana abierta
# Sin esta línea, la ventana se abriría y cerraría de inmediato.
root.mainloop()

