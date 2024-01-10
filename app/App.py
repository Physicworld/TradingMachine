import customtkinter as ctk
from . addBotWindow import AddBotWindow  # Asegúrate de que esta importación sea correcta según tu estructura de proyecto
from DatabaseConnection.DatabaseConnection import DatabaseConnection
from Models.Bot import Bot

# Establecer el modo de apariencia y el tema de color globalmente
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.title("Quantitative Machine")
        self.geometry("800x600")


        # Mostrar tabla de bots
        num_rows = self.showBotTable() + 1

        # Botón para añadir un nuevo bot
        buttonAddBot = ctk.CTkButton(self, text="Add Bot", command=lambda: AddBotWindow())
        buttonAddBot.grid(row=num_rows, column=3, columnspan=4, pady=10)


    def showBotTable(self):
        # self.databaseConnection = DatabaseConnection()

        bots = DatabaseConnection().readModel(Bot)
        print(bots)
        # Lista de ejemplo de bots
        bots = [{"nombre": "Bot1", "estado": "Activo"}, {"nombre": "Bot2", "estado": "Inactivo"}]

        for i, bot in enumerate(bots, start=1):  # Comienza en 1 para dejar espacio para el botón en la fila 0
            nombre_bot = ctk.CTkLabel(self, text=bot["nombre"])
            nombre_bot.grid(row=i, column=0, pady=5, padx=5)

            estado_bot = ctk.CTkLabel(self, text=bot["estado"])
            estado_bot.grid(row=i, column=1, pady=5, padx=5)

            boton_editar = ctk.CTkButton(self, text="Editar", command=lambda b=bot: self.editar_bot(b))
            boton_editar.grid(row=i, column=2, pady=5, padx=5)

            boton_eliminar = ctk.CTkButton(self, text="Eliminar", command=lambda b=bot: self.eliminar_bot(b))
            boton_eliminar.grid(row=i, column=3, pady=5, padx=5)
        return len(bots)

    def editar_bot(self, bot):
        # Lógica para editar el bot
        print("Editar", bot)

    def eliminar_bot(self, bot):
        # Lógica para eliminar el bot
        print("Eliminar", bot)

