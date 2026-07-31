from sqlalchemy.orm import Session
from app.models import Equipment


class EquipmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, quantity: int):
        equipment = Equipment(name=name, quantity=quantity)
        self.db.add(equipment)
        self.db.commit()
        self.db.refresh(equipment)
        return equipment

    def get_all(self):
        return self.db.query(Equipment).all()

    def get_by_id(self, equipment_id: int):
        return self.db.query(Equipment).filter(Equipment.id == equipment_id).first()

    def get_by_name(self, name: str):
        return self.db.query(Equipment).filter(Equipment.name == name).first()

    def update(self, equipment_id: int, name: str, quantity: int):
        equipment = self.get_by_id(equipment_id)
        if equipment:
            equipment.name = name
            equipment.quantity = quantity
            self.db.commit()
            self.db.refresh(equipment)
        return equipment

    def patch(self, equipment_id: int, name: str = None, quantity: int = None):
        equipment = self.get_by_id(equipment_id)
        if equipment:
            if name is not None:
                equipment.name = name
            if quantity is not None:
                equipment.quantity = quantity
            self.db.commit()
            self.db.refresh(equipment)
        return equipment

    def delete(self, equipment_id: int):
        equipment = self.get_by_id(equipment_id)
        if equipment:
            self.db.delete(equipment)
            self.db.commit()
        return equipment