from Models.Bot import Bot
def createBot(name, exchange, market_type, symbol, initial_balance, order_size, running):
    return Bot(
        name=name,
        exchange=exchange,
        market_type=market_type,
        symbol=symbol,
        initial_balance=initial_balance,
        current_balance=initial_balance,
        order_size=order_size,
        running=running,
    )
