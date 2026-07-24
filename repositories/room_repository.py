from sqlalchemy.orm import Session
from models import Room


class RoomRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, capacity: int):
        room = Room(name=name, capacity=capacity)
        self.db.add(room)
        self.db.commit()
        self.db.refresh(room)
        return room

    def get_all(self):
        return self.db.query(Room).all()

    def get_by_id(self, room_id: int):
        return self.db.query(Room).filter(Room.id == room_id).first()

    def get_by_name(self, name: str):
        return self.db.query(Room).filter(Room.name == name).first()

    def update(self, room_id: int, name: str, capacity: int):
        room = self.get_by_id(room_id)
        if room:
            room.name = name
            room.capacity = capacity
            self.db.commit()
            self.db.refresh(room)
        return room

    def patch(self, room_id: int, name: str = None, capacity: int = None):
        room = self.get_by_id(room_id)
        if room:
            if name is not None:
                room.name = name
            if capacity is not None:
                room.capacity = capacity
            self.db.commit()
            self.db.refresh(room)
        return room

    def delete(self, room_id: int):
        room = self.get_by_id(room_id)
        if room:
            self.db.delete(room)
            self.db.commit()
        return room