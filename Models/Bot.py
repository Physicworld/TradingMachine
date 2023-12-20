from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from . ModelBase import Base

class Bot(Base):
    __tablename__ = 'bots'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    market_type = Column(String)
    exchange = Column(String)
    initial_balance = Column(Float)
    current_balance = Column(Float)
    order_size = Column(Float)
    running = Column(Boolean)

