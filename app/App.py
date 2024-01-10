import tkinter as tk
from tkinter import ttk
from . AddBotWindow import AddBotWindow  # Asegúrate de que esta importación sea correcta según tu estructura de proyecto
from . BotTable import BotTable  # Asegúrate de que esta importación sea correcta según tu estructura de proyecto

# Establecer el modo de apariencia y el tema de color globalmente
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("green")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.title("Quantitative Machine")
        self.geometry("800x600")

        tableBotTable = BotTable(self)
        tableBotTable.pack(fill="both", expand=True)


        buttonAddBot = tk.Button(self, text="Add Bot", command=lambda: AddBotWindow())
        buttonAddBot.pack(pady=10)

        buttonEditBot = tk.Button(self, text="Edit Bot")
        buttonEditBot.pack(pady=10)

        buttonDeleteBot = tk.Button(self, text="Delete Bot")
        buttonDeleteBot.pack(pady=10)



