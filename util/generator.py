from util.rooms import rooms_dict
from adventure.models import Player, Room

def generate_room():
    for room in rooms_dict:
        room = Room(room['title'], room['description'])
        room.save()

