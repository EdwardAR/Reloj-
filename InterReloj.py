import tkinter as tk
from datetime import datetime
import random

# Colores para cambiar dinámicamente el texto
colores = ['red', 'green', 'blue', 'purple', 'orange', 'cyan']

def actualizar_hora():
    # Obtener la hora actual
    ahora = datetime.now().strftime("%H:%M:%S")
    
    # Cambiar el texto y el color de la hora
    etiqueta_hora.config(text=ahora, fg=random.choice(colores))
    
    # Programar la siguiente actualización en 1 segundo
    ventana.after(1000, actualizar_hora)

def cerrar_reloj():
    # Cierra la ventana de la aplicación
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Dinámico")
ventana.geometry("400x200")  # Tamaño de la ventana
ventana.configure(bg='lightgray')  # Color de fondo

# Crear una etiqueta para mostrar la hora
etiqueta_hora = tk.Label(ventana, font=("Helvetica", 48), bg='lightgray')
etiqueta_hora.pack(pady=20)

# Crear un botón para cerrar el reloj
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_reloj, font=("Helvetica", 14), bg='red', fg='white')
boton_cerrar.pack(pady=10)

# Llamar a la función para actualizar la hora por primera vez
actualizar_hora()

# Iniciar el loop principal de la ventana
ventana.mainloop()
