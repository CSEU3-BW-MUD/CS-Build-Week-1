from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.rooms import room_title, room_descriptions

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        x = -1
        y = 0
        room_count = 0
        direction = 1
        previous_room = None
        while room_count < num_rooms:

            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                room_direction = "n"
                y += 1
                direction *= -1
            room = Room(title=room_title[room_count],
                        description=room_descriptions[room_count], x=x, y=y)
            room.save()
            self.grid[y][x] = room

            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
            previous_room = room
            room_count += 1


# w = World()
# num_rooms = 100
# width = 10
# height = 10
# w.generate_rooms(width, height, num_rooms)
