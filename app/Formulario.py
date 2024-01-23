import tkinter as tk
from tkinter import ttk


class Formulario(tk.Toplevel):
    def __init__(self, parent, operacion, datos=None):
        super().__init__(parent)
        self.parent = parent
        self.operacion = operacion
        self.title(f"{operacion.capitalize()} Registro")

        self.nombre_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.ciudad_var = tk.StringVar()

        # Etiquetas y campos de entrada
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Edad:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.edad_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Ciudad:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.ciudad_var).grid(row=2, column=1, padx=10, pady=5)

        # Botón Aceptar
        tk.Button(self, text="Aceptar", command=self.aceptar).grid(row=3, column=0, columnspan=2, pady=10)

        if datos:
            # Si se proporcionan datos, llenar los campos
            self.nombre_var.set(datos[0])
            self.edad_var.set(datos[1])
            self.ciudad_var.set(datos[2])

    def aceptar(self):
        # Obtener los valores ingresados
        nombre = self.nombre_var.get()
        edad = self.edad_var.get()
        ciudad = self.ciudad_var.get()

        # Validar los datos si es necesario

        # Realizar la operación según el modo (Agregar o Editar)
        if self.operacion == "agregar":
            self.parent.agregar_elemento(nombre, edad, ciudad)
        elif self.operacion == "editar":
            self.parent.editar_elemento(nombre, edad, ciudad)

        # Cerrar la ventana después de aceptar
        self.destroy()