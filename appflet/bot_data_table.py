import flet as ft

from Models.Bot import Bot
from DatabaseConnection.DatabaseConnection import DatabaseConnection

class BotDataTable:
    def __init__(self):
        bot = Bot()
        headers = vars(bot).keys()  # Obtiene los nombres de los atributos de Bot

        self.bots = DatabaseConnection().readModel(Bot)  # Lee los objetos Bot de la base de datos

        self.columns = [
            ft.DataColumn(label=ft.Text(head)) for head in headers
        ]  # Crea las columnas para el DataTable

        self.rows = [
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(str(getattr(bot, head)))) for head in headers]
            ) for bot in self.bots
        ]  # Crea las filas para el DataTable

        self.control = ft.DataTable(columns=self.columns, rows=self.rows)  # Crea el control DataTable