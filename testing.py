from dungeon_game.items import *
from dungeon_game.entities import *

bob = human('bob', 5)
bob.health = 50
print(bob.health)
item = test_item(bob)
bob.inventory.get_item(item)
print(bob.inventory.inv[0].stack)
bob.inventory.inv[0].stack[0].use()
print(bob.health)