import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabla con Treeview")

# 1. Crear el Treeview
tree = ttk.Treeview(root, columns=("A", "B", "C"), show="headings")

# 2. Definir encabezados de columna
tree.heading("A", text="Nombre")
tree.heading("B", text="Edad")
tree.heading("C", text="País")

# 3. Insertar datos (filas)
data = [
    ("Alice", 30, "USA"),
    ("Bob", 22, "Canadá"),
    ("Charlie", 45, "México")
]

for item in data:
    # Inserta cada elemento como una nueva fila.
    tree.insert("", tk.END, values=item)

# 4. Empaquetar el widget
tree.pack(pady=10, padx=10)

root.mainloop()