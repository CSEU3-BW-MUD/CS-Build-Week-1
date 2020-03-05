from util.new_create_world import World
from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

testvar = World()

num_rooms = 100
width = 10
height = 10

testvar.generate_rooms(width, height, num_rooms)