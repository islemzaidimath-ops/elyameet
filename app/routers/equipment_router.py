from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.equipment_repository import EquipmentRepository
from app.services.equipment_service import EquipmentService

router = APIRouter(prefix="/equipments", tags=["Equipments"])


def get_service(db: Session = Depends(get_db)):
    repository = EquipmentRepository(db)
    return EquipmentService(repository)


@router.post("/")
def create_equipment(name: str, quantity: int, service: EquipmentService = Depends(get_service)):
    return service.create_equipment(name, quantity)


@router.get("/")
def list_equipments(service: EquipmentService = Depends(get_service)):
    return service.list_equipments()


@router.get("/{equipment_id}")
def get_equipment(equipment_id: int, service: EquipmentService = Depends(get_service)):
    return service.get_equipment(equipment_id)


@router.put("/{equipment_id}")
def update_equipment(equipment_id: int, name: str, quantity: int, service: EquipmentService = Depends(get_service)):
    return service.update_equipment(equipment_id, name, quantity)


@router.patch("/{equipment_id}")
def patch_equipment(equipment_id: int, name: str = None, quantity: int = None, service: EquipmentService = Depends(get_service)):
    return service.patch_equipment(equipment_id, name, quantity)


@router.delete("/{equipment_id}")
def delete_equipment(equipment_id: int, service: EquipmentService = Depends(get_service)):
    return service.delete_equipment(equipment_id)