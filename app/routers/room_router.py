from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.room_repository import RoomRepository
from app.services.room_service import RoomService

router = APIRouter(prefix="/rooms", tags=["Rooms"])


def get_service(db: Session = Depends(get_db)):
    repository = RoomRepository(db)
    return RoomService(repository)


@router.post("/")
def create_room(name: str, capacity: int, service: RoomService = Depends(get_service)):
    return service.create_room(name, capacity)


@router.get("/")
def list_rooms(service: RoomService = Depends(get_service)):
    return service.list_rooms()


@router.get("/{room_id}")
def get_room(room_id: int, service: RoomService = Depends(get_service)):
    return service.get_room(room_id)


@router.put("/{room_id}")
def update_room(room_id: int, name: str, capacity: int, service: RoomService = Depends(get_service)):
    return service.update_room(room_id, name, capacity)


@router.patch("/{room_id}")
def patch_room(room_id: int, name: str = None, capacity: int = None, service: RoomService = Depends(get_service)):
    return service.patch_room(room_id, name, capacity)


@router.delete("/{room_id}")
def delete_room(room_id: int, service: RoomService = Depends(get_service)):
    return service.delete_room(room_id)

