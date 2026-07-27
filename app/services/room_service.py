from fastapi import HTTPException


class RoomService:
    def __init__(self, repository):
        self.repository = repository

    def create_room(self, name: str, capacity: int):
        if capacity <= 0:
            raise HTTPException(400, "La capacité doit être positive")

        if self.repository.get_by_name(name):
            raise HTTPException(400, "Une salle avec ce nom existe déjà")

        return self.repository.create(name, capacity)

    def list_rooms(self):
        return self.repository.get_all()

    def get_room(self, room_id: int):
        room = self.repository.get_by_id(room_id)
        if not room:
            raise HTTPException(404, "Salle introuvable")
        return room

    def update_room(self, room_id: int, name: str, capacity: int):
        self.get_room(room_id)

        if capacity <= 0:
            raise HTTPException(400, "La capacité doit être strictement positive")

        existing = self.repository.get_by_name(name)
        if existing and existing["id"] != room_id:
            raise HTTPException(400, "Une salle avec ce nom existe déjà")

        return self.repository.update(room_id, name, capacity)

    def patch_room(self, room_id: int, name: str = None, capacity: int = None):
        self.get_room(room_id)

        if capacity is not None and capacity <= 0:
            raise HTTPException(400, "La capacité doit être srictement positive")

        if name is not None:
            existing = self.repository.get_by_name(name)
            if existing and existing["id"] != room_id:
                raise HTTPException(400, "Une salle avec ce nom existe déjà")

        return self.repository.patch(room_id, name, capacity)

    def delete_room(self, room_id: int):
        self.get_room(room_id)
        return self.repository.delete(room_id)