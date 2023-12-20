import tkinter as tk
import customtkinter as ctk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models.Bot import Bot

exchanges = ["Binance"]
market_types = ["Spot", "Futures"]
symbols = ["BTC/USDT", "ETH/USDT", "LTC/USDT"]

def save_bot_callback(name, exchange, market_type, symbol, initial_balance, order_size, running):
    print("Saving Bot!")
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    new_bot = Bot(
        name=name,
        exchange=exchange,
        market_type=market_type,
        symbol=symbol,
        initial_balance=initial_balance,
        current_balance=initial_balance,
        order_size=order_size,
        running=running,
    )
    session.add(new_bot)
    session.commit()
    session.close()


def add_bot():
    newWindow = ctk.CTkToplevel()
    newWindow.title("Add Bot")

    nameLabel = ctk.CTkLabel(newWindow, text="Name")
    nameLabel.pack(pady=10)
    nameEntry = ctk.CTkEntry(newWindow)
    nameEntry.pack()


    exchangeLabel = ctk.CTkLabel(newWindow, text="Exchange")
    exchangeLabel.pack(pady=10)
    exchangeDropdown = ctk.CTkOptionMenu(newWindow, values=exchanges)
    exchangeDropdown.pack(pady=10)

    marketTypeLabel = ctk.CTkLabel(newWindow, text="Market Type")
    marketTypeLabel.pack(pady=10)
    marketTypeDropdown = ctk.CTkOptionMenu(newWindow, values=market_types)
    marketTypeDropdown.pack(pady=10)

    symbolLabel = ctk.CTkLabel(newWindow, text="Symbol")
    symbolLabel.pack(pady=10)
    symbolDropdown = ctk.CTkOptionMenu(newWindow, values=symbols)
    symbolDropdown.pack(pady=10)

    initialBalanceLabel = ctk.CTkLabel(newWindow, text="Initial Balance")
    initialBalanceLabel.pack(pady=10)
    initialBalanceEntry = ctk.CTkEntry(newWindow)
    initialBalanceEntry.pack(pady=10)

    orderSizeLabel = ctk.CTkLabel(newWindow, text="Order Size")
    orderSizeLabel.pack(pady=10)
    orderSizeEntry = ctk.CTkEntry(newWindow)
    orderSizeEntry.pack(pady=10)

    runningLabel = ctk.CTkLabel(newWindow, text="Running")
    runningLabel.pack(pady=10)
    runningSwitch = ctk.CTkSwitch(newWindow, text="True")
    runningSwitch.pack(pady=10)


    saveButton = ctk.CTkButton(
        newWindow,
        text="Save",
        command=lambda: save_bot_callback(nameEntry.get(), exchangeDropdown.get(), marketTypeDropdown.get(), symbolDropdown.get(), initialBalanceEntry.get(), orderSizeEntry.get(), runningSwitch.get())
    )
    saveButton.pack(pady=10)


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()

buttonAddBot = ctk.CTkButton(app, text="Add Bot", command=add_bot)
buttonAddBot.pack(pady=10)

app.mainloop()
