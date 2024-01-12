import flet as ft
from appflet.app_view import AppView

def main(page: ft.Page):
    app_view = AppView(page)
    app_view.render()

ft.app(target=main)
