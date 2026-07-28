from unittest.mock import Mock
from app.services.room_service import RoomService

fake_repository = Mock()
fake_repository.get_by_name.return_value = None
fake_repository.create.return_value = {"id": 1, "name": "Salle A", "capacity": 20}

service = RoomService(fake_repository)
resultat = service.create_room("Salle A", 20)

print("Résultat :", resultat)
assert resultat["name"] == "Salle A"
print("Test réussi !") 



    

 

