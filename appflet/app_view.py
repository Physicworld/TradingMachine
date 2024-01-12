import flet as ft
from . bot_data_table import BotDataTable
from . bot_actions import add_bot, edit_bot, delete_bot

class AppView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.data_table = BotDataTable()

    def render(self):
        add_bot_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_bot)
        edit_bot_button = ft.FloatingActionButton(icon=ft.icons.EDIT, on_click=edit_bot)
        delete_bot_button = ft.FloatingActionButton(icon=ft.icons.DELETE, on_click=delete_bot)

        controls = [self.data_table.control, add_bot_button, edit_bot_button, delete_bot_button]
        view = ft.Column(controls=controls, spacing=10)

        self.page.add(view)
