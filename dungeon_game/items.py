#for setting up items/ inventory
from random import randint
weapons = ['axe', 'sword', 'mace', 'whip']
weapon_dmg = [3, 5, 4, 2]

class inventory:
    def __init__(self, user):
        self.inv = [slot(0, user), slot(1, user), slot(2, user), slot(3, user)]
    
    def get_item(self, item):
        c = 0
        for slot in self.inv: #looping by objects is better than ranges!
            if len(slot.stack) != 5 and slot.item_id == item.id:
                slot.stack.append(item)
                break
            else:
                c = c + 1
                continue
        if c == 4:
            print('slots full!')
    
    def use_item(self, stack_id):
        for slot in self.inv:
            if slot.item_id == stack_id and len(slot.stack) != 0:
                slot.stack[0].use()
                slot.stack.pop()
            else:
                continue

    def __str__(self):
        rtnstr = '' 
        for slot in self.inv:
            try: #Since each stack can only hold one type of item, we only need to check the first index and get the length to determine what is in the stack
                rtnstr = rtnstr + f'{slot.item_id}: {slot.stack[0]} #{len(slot.stack)} \n ---------------------- \n' 
            except: 
                continue # An error can only occur if the stack is empty, so continue to the next stack if a failure occurs
        return rtnstr


class slot:
        def __init__(self, id, name):
            self.stack = []
            self.item_id = id
            self.user = name

    
class test_item:
    def __init__(self, user):
        self.id = 0 # ids denote what inv slot an item goes into
        self.type = 'testing'
        self.actions = {'heal': 20, 'super heal': 100}
        self.action_list = {1: 'heal', 2: 'super heal'}
        self.user = user
    
    def use(self):
        run = 1
        for k, v in self.actions.items():
            print(f'{run}: {k}')
            run = run + 1
        choice = input('pick an action: ')
        for k, v in self.action_list.items():
            if k == int(choice.strip()):
                self.heal(self.actions.get(v), self.user)
                break
            else:
                continue
    
    def heal(self, amt, target):
        target.health = target.health + amt
    
    def __str__(self):
        return "Testing item"

class dummy_item: #this is an item that just takes up a random slot when it is picked up, for testing only!!!
    def __init__(self):
        self.id = 3

    def __str__(self):
        return "dummy item"

class life_drop:
    def __init__(self, amt, player):
        self.id = 00 # double zero id is not an inv item, it'll make sense when the drop sys is implmented. i hope
        self.heal_amt = amt
        self.playerhealth = player.health
        self.heal(self.heal_amt)
        player.health = self.playerhealth

    def heal(self, heal_amt):
        self.playerhealth = self.playerhealth + heal_amt

class weapon:
    pass


