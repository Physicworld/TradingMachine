import customtkinter as ctk
from Factory.BotFactory import createBot
from DatabaseConnection.DatabaseConnection import DatabaseConnection

exchanges = ["Binance"]
market_types = ["Spot", "Futures"]
symbols = ["BTC/USDT", "ETH/USDT", "LTC/USDT"]


class AddBotWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.init_gui()
        self.db = DatabaseConnection()

    def init_gui(self):
        self.title("Add Bot")
        self.geometry("400x800")

        self.nameLabel = ctk.CTkLabel(self, text="Name")
        self.nameLabel.pack(pady=10)
        self.nameEntry = ctk.CTkEntry(self)
        self.nameEntry.pack()

        self.exchangeLabel = ctk.CTkLabel(self, text="Exchange")
        self.exchangeLabel.pack(pady=10)
        self.exchangeDropdown = ctk.CTkOptionMenu(self, values=exchanges)
        self.exchangeDropdown.pack(pady=10)

        self.marketTypeLabel = ctk.CTkLabel(self, text="Market Type")
        self.marketTypeLabel.pack(pady=10)
        self.marketTypeDropdown = ctk.CTkOptionMenu(self, values=market_types)
        self.marketTypeDropdown.pack(pady=10)

        self.symbolLabel = ctk.CTkLabel(self, text="Symbol")
        self.symbolLabel.pack(pady=10)
        self.symbolDropdown = ctk.CTkOptionMenu(self, values=symbols)
        self.symbolDropdown.pack(pady=10)

        self.initialBalanceLabel = ctk.CTkLabel(self, text="Initial Balance")
        self.initialBalanceLabel.pack(pady=10)
        self.initialBalanceEntry = ctk.CTkEntry(self)
        self.initialBalanceEntry.pack(pady=10)

        self.orderSizeLabel = ctk.CTkLabel(self, text="Order Size")
        self.orderSizeLabel.pack(pady=10)
        self.orderSizeEntry = ctk.CTkEntry(self)
        self.orderSizeEntry.pack(pady=10)

        self.runningLabel = ctk.CTkLabel(self, text="Running")
        self.runningLabel.pack(pady=10)
        self.runningSwitch = ctk.CTkSwitch(self, text="True")
        self.runningSwitch.pack(pady=10)

        self.saveButton = ctk.CTkButton(
            self,
            text="Save",
            command=lambda: self.save_bot_callback()
        )
        self.saveButton.pack(pady=10)

    def save_bot_callback(self):
        newBot = createBot(
            name=self.nameEntry.get(),
            exchange=self.exchangeDropdown.get(),
            market_type=self.marketTypeDropdown.get(),
            symbol=self.symbolDropdown.get(),
            initial_balance=self.initialBalanceEntry.get(),
            order_size=self.orderSizeEntry.get(),
            running=self.runningSwitch.get()
        )
        print(newBot)
        self.db.saveModel(newBot)



