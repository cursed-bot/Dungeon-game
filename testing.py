from dungeon_game.items import *

test = inventory()
test.get_item('test')
print(test.inv[0].stack)
