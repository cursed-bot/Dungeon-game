# this file is for test in progress features 
from dungeon_game.items import *
from dungeon_game.entities import *

bob = human('bob', 5)
bob.health = 50
print(bob.health)
item = test_item(bob)
item2 = dummy_item()
item3 = dummy_item()
item4 = dummy_item()
item5 = dummy_item()
item6 = dummy_item()
item7 = dummy_item()

bob.inventory.get_item(item)
bob.inventory.get_item(item2)
bob.inventory.get_item(item3)
bob.inventory.get_item(item4)
bob.inventory.get_item(item5)
bob.inventory.get_item(item6)
bob.inventory.get_item(item7)

print(bob.inventory)
bob.inventory.use_item(0)
print(bob.health)