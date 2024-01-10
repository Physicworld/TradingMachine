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

    def __repr__(self):
        return "<Bot(name='%s', symbol='%s', market_type='%s', exchange='%s', initial_balance='%s', current_balance='%s', order_size='%s', running='%s')>" % (
            self.name,
            self.symbol,
            self.market_type,
            self.exchange,
            self.initial_balance,
            self.current_balance,
            self.order_size,
            self.running,
        )
