import tkinter as tk
from tkinter import ttk
from app.BotTable import Tabla

class AplicacionPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Principal")

        # Crear la instancia de la clase Tabla y pasar la ventana principal como padre
        self.tabla = Tabla(self)
        self.tabla.pack(padx=10, pady=10)  # Llamar al método pack aquí


if __name__ == "__main__":
    app = AplicacionPrincipal()
    app.mainloop()
