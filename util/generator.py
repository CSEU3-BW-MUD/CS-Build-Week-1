from util.rooms import rooms_dict
from adventure.models import Player, Room

def generate_room():
    for key, value in rooms_dict.items():
        key = Room(title=value['title'], description=value['description'])
        key.save()

