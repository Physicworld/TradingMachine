import flet as ft

from . bot_dialog import BotAddDialog, BotEditDialog

def add_bot(e):
    # Muestra el diálogo para añadir un bot
    dialog = BotAddDialog()
    dialog.show()

def edit_bot(e):
    # Muestra el diálogo para editar un bot
    dialog = BotEditDialog()
    dialog.show()

def delete_bot(e):
    # Lógica para eliminar un bot
    pass
