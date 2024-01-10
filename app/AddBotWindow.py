import tkinter as tk
from tkinter import ttk
from Factory.BotFactory import createBot
from DatabaseConnection.DatabaseConnection import DatabaseConnection

exchanges = ["Binance"]
market_types = ["Spot", "Futures"]
symbols = ["BTC/USDT", "ETH/USDT", "LTC/USDT"]
strategies = ["GridBot", "MeanReversion"]

class AddBotWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.render()
        self.db = DatabaseConnection()

    def render(self):
        self.title("Add Bot")
        self.geometry("400x960")

        # Use StringVar for dropdowns and IntVar for Checkbutton
        self.value_exchange = tk.StringVar(value=exchanges[0])
        self.value_market_type = tk.StringVar(value=market_types[0])
        self.value_symbol = tk.StringVar(value=symbols[0])
        self.value_strategy = tk.StringVar(value=strategies[0])
        self.running_state = tk.IntVar(value=0)

        self.nameLabel = tk.Label(self, text="Name")
        self.nameLabel.pack(pady=10)
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        self.exchangeLabel = tk.Label(self, text="Exchange")
        self.exchangeLabel.pack(pady=10)
        self.exchangeDropdown = tk.OptionMenu(self, self.value_exchange, *exchanges)
        self.exchangeDropdown.pack(pady=10)

        self.marketTypeLabel = tk.Label(self, text="Market Type")
        self.marketTypeLabel.pack(pady=10)
        self.marketTypeDropdown = tk.OptionMenu(self, self.value_market_type, *market_types)
        self.marketTypeDropdown.pack(pady=10)

        self.symbolLabel = tk.Label(self, text="Symbol")
        self.symbolLabel.pack(pady=10)
        self.symbolDropdown = tk.OptionMenu(self, self.value_symbol, *symbols)
        self.symbolDropdown.pack(pady=10)

        self.strategyLabel = tk.Label(self, text="Strategy")
        self.strategyLabel.pack(pady=10)
        self.strategyDropdown = tk.OptionMenu(self, self.value_strategy, *strategies)
        self.strategyDropdown.pack(pady=10)

        self.strategyParamsLabel = tk.Label(self, text="Strategy Params")
        self.strategyParamsLabel.pack(pady=10)
        self.strategyParamsEntry = tk.Entry(self)
        self.strategyParamsEntry.pack(pady=10)

        self.initialBalanceLabel = tk.Label(self, text="Initial Balance")
        self.initialBalanceLabel.pack(pady=10)
        self.initialBalanceEntry = tk.Entry(self)
        self.initialBalanceEntry.pack(pady=10)

        self.orderSizeLabel = tk.Label(self, text="Order Size")
        self.orderSizeLabel.pack(pady=10)
        self.orderSizeEntry = tk.Entry(self)
        self.orderSizeEntry.pack(pady=10)

        self.runningLabel = tk.Label(self, text="Running")
        self.runningLabel.pack(pady=10)
        self.runningSwitch = tk.Checkbutton(self, text="True", variable=self.running_state)
        self.runningSwitch.pack(pady=10)

        self.saveButton = tk.Button(self, text="Save", command=self.save_bot_callback)
        self.saveButton.pack(pady=10)

    def save_bot_callback(self):
        newBot = createBot(
            name=self.nameEntry.get(),
            exchange=self.value_exchange.get(),
            strategy=self.value_strategy.get(),
            strategy_params=self.strategyParamsEntry.get(),
            market_type=self.value_market_type.get(),
            symbol=self.value_symbol.get(),
            initial_balance=self.initialBalanceEntry.get(),
            order_size=self.orderSizeEntry.get(),
            running=bool(self.running_state.get())
        )
        print(newBot)
        self.db.saveModel(newBot)
