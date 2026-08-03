from sqlalchemy import Column, Integer, String
from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)

class Equipment(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)

