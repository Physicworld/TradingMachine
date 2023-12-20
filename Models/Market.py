from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from . ModelBase import Base

class Market(Base):
    __tablename__ = 'markets'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    market_type = Column(String)
    exchange = Column(String)
    minQty = Column(Float)
    pricePrecision = Column(Integer)
    quantityPrecision = Column(Integer)