# this file is for test in progress features 

from dungeon_game.entities import monster, human


class slime(monster):
    def __init__(self, *args):
        try:
            self.id = args[0]
            super().__init__("slime", 1, 5, 2)
        except:
            super().__init__("slime", 1, 5, 2)
    
    def take_damage(self, dmg, attacker): 
        if self.alive == False:
            print("{} is already dead!".format(self.species))
        elif (self.health - dmg) <= 0:
            self.health = 0
            self.mdeath(attacker)
        else:
            self.health = self.health - dmg
        
    def mdeath(self, target):
        super().death()
        print(f'{self.species} dropped 10 life!')
        life_drop(2, target)

bob = human('bob', 5)

slime = slime()

bob.attack(slime)
