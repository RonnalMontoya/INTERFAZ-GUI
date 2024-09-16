import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

# Función para agregar elementos a la lista
def agregar_item():
    item = entrada_texto.get()
    if item:
        lista_items.insert(tk.END, item)  # Agregar al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista_items.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Etiqueta
etiqueta = tk.Label(root, text="Ingrese un elemento:")
etiqueta.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(root, width=30)
entrada_texto.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(root, text="Agregar", command=agregar_item)
boton_agregar.pack(pady=5)

# Lista para mostrar los elementos
lista_items = tk.Listbox(root, width=40, height=10)
lista_items.pack(pady=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
