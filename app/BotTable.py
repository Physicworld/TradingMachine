
import tkinter as tk
from tkinter import ttk
from Models.Bot import Bot
from DatabaseConnection.DatabaseConnection import DatabaseConnection

class BotTable(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_styles()
        self.render()

    def init_styles(self):
        style = ttk.Style(self.parent)
        style.configure('Treeview', rowheight=25)  # Aumentar el tamaño de las filas
        style.configure('Treeview.Heading', font=('Calibri', 10, 'bold'))  # Estilo para los encabezados
        style.configure('Treeview', background='#E3F2FD', foreground='black',
                        fieldbackground='#E3F2FD')  # Estilo para las filas
        style.map('Treeview', background=[('selected', '#90CAF9')])  # Color cuando se selecciona una fila

    def render(self):
        self.canvas = tk.Canvas(self.parent, borderwidth=0, background="#ffffff")
        self.scrollbar = ttk.Scrollbar(self.parent, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.renderBotTable(self.scrollable_frame)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="left", fill="y")

    def renderBotTable(self, parent_frame):
        bots = DatabaseConnection().readModel(Bot)

        self.tree = ttk.Treeview(parent_frame, columns=('name', 'symbol', 'market_type', 'exchange', 'strategy', 'initial_balance', 'current_balance', 'order_size', 'running'), show='headings', selectmode='browse')
        self.tree.heading('name', text='Name')
        self.tree.heading('symbol', text='Symbol')
        self.tree.heading('market_type', text='Market Type')
        self.tree.heading('exchange', text='Exchange')
        self.tree.heading('strategy', text='Strategy')
        self.tree.heading('initial_balance', text='Initial Balance')
        self.tree.heading('current_balance', text='Current Balance')
        self.tree.heading('order_size', text='Order Size')
        self.tree.heading('running', text='Running')

        for i, bot in enumerate(bots, start=1):
            self.tree.insert('', 'end', values=(bot.name, bot.symbol, bot.market_type, bot.exchange, bot.strategy, bot.initial_balance, bot.current_balance, bot.order_size, "Yes" if bot.running else "No"))

        self.tree.grid(row=0, column=0, sticky='nsew')
        parent_frame.grid_rowconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)


#
# def editar_bot(self, bot):
#     # Lógica para editar el bot
#     print("Editar", bot)
#
#
# def eliminar_bot(self, bot):
#     # Lógica para eliminar el bot
#     print("Eliminar", bot)
