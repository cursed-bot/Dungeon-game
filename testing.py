# this file is for test in progress features 
from dungeon_game.items import *
from dungeon_game.entities import *

bob = human('bob', 5)
bob.health = 50
print(bob.health)
life_drop(50, bob)
print(bob.health)