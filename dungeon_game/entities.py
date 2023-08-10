from random import randint
from dungeon_game.items import *

weapons = ['axe', 'sword', 'mace', 'whip']
weapon_dmg = [3, 5, 4, 2]
class human:

    def __init__(self, name, dmg):
        self.health = 100
        self.alive = True
        self.name = name
        self.inventory = inventory(name)
        #weapon = randint(1, 3)
        #self.weapon = weapons[weapon]
        self.dmg = dmg #+ weapon_dmg[weapon]

    def __str__(self):
        if self.alive == False:
            dead = 'dead'
        else:
            dead = 'alive'

        return "{} is {}, has a {}, and has {} health left".format(self.name, dead, self.weapon, self.health)
    
    def death(self):
        self.health = 0
        self.alive = False
        print("{} died!".format(self.name))
    
    def take_damage(self, dmg):
        if self.alive == False:
            print("{} is already dead!".format(self.name))
        elif (self.health - dmg) <= 0:
            self.health = 0
            self.death()
        else:
            self.health = self.health - dmg
    
    def attack(self, target):
        if self.alive == False:
            pass
        else:
            target.take_damage(self.dmg, self)
    

class monster:

    def __init__(self, species, h_min, h_max, dmg):
        self.health = randint(h_min, h_max)
        self.species = species
        self.alive = True
        self.dmg = dmg
        self.counted = False

    def __str__(self):
        if self.alive == False:
            dead = 'dead'
        else:
            dead = 'alive'

        return "{} is {} and has {} health left".format(self.species, dead, self.health)
    
    def death(self):
        self.alive = False
        print("{} died!".format(self.species))
        
    
    def attack(self, target):
        if self.alive == False:
            pass
        else:
            target.take_damage(self.dmg)

class slime(monster):
    def __init__(self, *args):
        try:
            self.id = args[0]
            super().__init__("slime", 5, 15, 2)
        except:
            super().__init__("slime", 5, 15, 2)
    
    def take_damage(self, dmg, attacker): 
        if self.alive == False:
            print("{} is already dead!".format(self.species))
        elif (self.health - dmg) <= 0:
            self.health = 0
            self.mdeath(attacker)
        else:
            self.health = self.health - dmg
        
    def mdeath(self, target):
        super().death(self)
        print(f'{self.species} dropped 10 life!')
        life_drop(2, target)

class goblin(monster):
    def __init__(self, *args):
        try:
            self.id = args[0]
            super().__init__("goblin", 10, 20, 2)
        except:
            super().__init__("goblin", 10, 20, 2)

    def mdeath(self, target):
        super().death(self)
        life_drop(5, target)

    def take_damage(self, dmg, attacker): 
        if self.alive == False:
            print("{} is already dead!".format(self.species))
        elif (self.health - dmg) <= 0:
            self.health = 0
            self.mdeath(attacker)
        else:
            self.health = self.health - dmg