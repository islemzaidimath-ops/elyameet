from fastapi import HTTPException


class EquipmentService:
    def __init__(self, repository):
        self.repository = repository

    def create_equipment(self, name: str, quantity: int):
        if quantity <= 0:
            raise HTTPException(400, "La quantité doit être positive")
        if self.repository.get_by_name(name):
            raise HTTPException(400, "Un équipement avec ce nom existe déjà")
        return self.repository.create(name, quantity)

    def list_equipments(self):
        return self.repository.get_all()

    def get_equipment(self, equipment_id: int):
        equipment = self.repository.get_by_id(equipment_id)
        if not equipment:
            raise HTTPException(404, "Équipement introuvable")
        return equipment

    def update_equipment(self, equipment_id: int, name: str, quantity: int):
        self.get_equipment(equipment_id)
        if quantity <= 0:
            raise HTTPException(400, "La quantité doit être positive")
        existing = self.repository.get_by_name(name)
        if existing and existing.id != equipment_id:
            raise HTTPException(400, "Un équipement avec ce nom existe déjà")
        return self.repository.update(equipment_id, name, quantity)

    def patch_equipment(self, equipment_id: int, name: str = None, quantity: int = None):
        self.get_equipment(equipment_id)
        if quantity is not None and quantity <= 0:
            raise HTTPException(400, "La quantité doit être positive")
        if name is not None:
            existing = self.repository.get_by_name(name)
            if existing and existing.id != equipment_id:
                raise HTTPException(400, "Un équipement avec ce nom existe déjà")
        return self.repository.patch(equipment_id, name, quantity)

    def delete_equipment(self, equipment_id: int):
        self.get_equipment(equipment_id)
        return self.repository.delete(equipment_id)