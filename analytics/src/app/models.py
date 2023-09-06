from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date

from .database import Base


class Daily(Base):
    __tablename__ = "daily"

    index = Column(Integer, primary_key=True, index=True)
    fund_symbol = Column(String)
    date = Column(Date)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    adj_close_price = Column(Float)
    volume = Column(Integer)

    def __repr__(self):
        return f"<Daily(fund_symbol={self.fund_symbol}, date={self.date}, open_price={self.open_price}, high_price={self.high_price}, low_price={self.low_price}, close_price={self.close_price}, adj_close_price={self.adj_close_price}, volume={self.volume})>"
    
    def to_json(self):
        return {
            "fund_symbol": self.fund_symbol,
            "date": self.date,
            "open_price": self.open_price,
            "high_price": self.high_price,
            "low_price": self.low_price,
            "close_price": self.close_price,
            "adj_close_price": self.adj_close_price,
            "volume": self.volume
        }
