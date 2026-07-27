from fastapi import APIRouter
from repositories.room_repository import RoomRepository
from services.room_service import RoomService

router = APIRouter(prefix="/rooms", tags=["Rooms"])

repository = RoomRepository()
service = RoomService(repository)


@router.post("/")
def create_room(name: str, capacity: int):
    return service.create_room(name, capacity)


@router.get("/")
def list_rooms():
    return service.list_rooms()


@router.get("/{room_id}")
def get_room(room_id: int):
    return service.get_room(room_id)


@router.put("/{room_id}")
def update_room(room_id: int, name: str, capacity: int):
    return service.update_room(room_id, name, capacity)


@router.patch("/{room_id}")
def patch_room(room_id: int, name: str = None, capacity: int = None):
    return service.patch_room(room_id, name, capacity)


@router.delete("/{room_id}")
def delete_room(room_id: int):
    return service.delete_room(room_id)

