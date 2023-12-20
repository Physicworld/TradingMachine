from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from . ModelBase import Base
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    timestamp = Column(Integer)
    symbol = Column(String)
    market_type = Column(String)
    exchange = Column(String)
    order_type = Column(String)
    side = Column(String)
    quantity = Column(Float)