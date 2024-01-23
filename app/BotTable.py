import tkinter as tk
from tkinter import ttk
from .Formulario import Formulario

class Tabla(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.datos = [
            ("Juan", 25, "Ciudad A"),
            ("María", 30, "Ciudad B"),
            ("Carlos", 22, "Ciudad C"),
        ]
        self.inicializar_tabla()
        self.inicializar_botones()

    def inicializar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        for i, values in enumerate(self.datos):
            self.tabla.insert(
                parent="",
                index="end",
                iid=i,
                values=values
            )

    def inicializar_tabla(self):
        # Crear el Treeview (tabla)
        self.tabla = ttk.Treeview(self)

        # Definir columnas
        self.tabla["columns"] = ("Nombre", "Edad", "Ciudad")

        # Configurar encabezados de columna
        self.tabla.column("#0", width=0, stretch=tk.NO)  # Columna invisible para índices
        self.tabla.column("Nombre", anchor=tk.W, width=100)
        self.tabla.column("Edad", anchor=tk.CENTER, width=50)
        self.tabla.column("Ciudad", anchor=tk.W, width=100)

        # Configurar encabezados de columna
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Nombre", text="Nombre", anchor=tk.W)
        self.tabla.heading("Edad", text="Edad", anchor=tk.CENTER)
        self.tabla.heading("Ciudad", text="Ciudad", anchor=tk.W)

        # Agregar datos a la tabla
        self.tabla.insert(parent="", index="end", iid=0, values=("Juan", 25, "Ciudad A"))
        self.tabla.insert(parent="", index="end", iid=1, values=("María", 30, "Ciudad B"))
        self.tabla.insert(parent="", index="end", iid=2, values=("Carlos", 22, "Ciudad C"))

        # Vincular el evento de clic a la tabla
        self.tabla.bind("<ButtonRelease-1>", self.obtener_seleccion)

        # Empaquetar la tabla en el contenedor
        self.tabla.pack(padx=10, pady=10)

    def inicializar_botones(self):
        # Botón para agregar nuevo elemento
        btn_agregar = tk.Button(self, text="Agregar", command=self.abrir_formulario_agregar)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para editar elemento
        btn_editar = tk.Button(self, text="Editar", command=self.abrir_formulario_editar())
        btn_editar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar elemento
        btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_elemento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

    def obtener_seleccion(self, event):
        item = self.tabla.selection()[0]  # Obtener el ID del ítem seleccionado
        valores = self.tabla.item(item, "values")
        print("Fila seleccionada:", valores)

    def abrir_formulario_agregar(self):
        formulario = Formulario(self, "agregar")
        self.wait_window(formulario)

    def abrir_formulario_editar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            valores = self.tabla.item(item, "values")
            formulario = Formulario(self, "editar", valores)
            self.wait_window(formulario)
        else:
            print("No hay elementos seleccionados")

    def agregar_elemento(self, nombre, edad, ciudad):
        # Aquí puedes implementar la lógica para agregar un nuevo elemento a la tabla
        self.datos.append((nombre, edad, ciudad))
        self.tabla.insert(parent="", index="end", iid=len(self.datos) - 1, values=(nombre, edad, ciudad))
        print(f"Agregar: {nombre}, {edad}, {ciudad}")

    def editar_elemento(self, nombre, edad, ciudad):
        # Aquí puedes implementar la lógica para editar el elemento seleccionado de la tabla
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            self.tabla.item(item, values=(nombre, edad, ciudad))
            print(f"Editar: {nombre}, {edad}, {ciudad}")
        else:
            print("No hay elementos seleccionados")
    def eliminar_elemento(self):
        # Implementar la lógica para eliminar un elemento de la tabla
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            self.tabla.delete(item)
            print("Eliminar elemento")
        else:
            print("Selecciona una fila para eliminar")