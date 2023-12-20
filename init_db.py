from sqlalchemy import create_engine
from Models.ModelBase import Base
from Models.Order import Order
from Models.Market import Market
from Models.Bot import Bot

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)