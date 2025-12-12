from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Column, Integer, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


# Board model for database
class Board(Base):
    __tablename__ = "board"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(64))
    created_time: datetime = Column(DateTime)