#for setting up items/ inventory

class inventory:
    def __init__(self, user):
        self.inv = [slot(0, user), slot(1, user), slot(2, user), slot(3, user)]
    
    def get_item(self, item):
        c = 0
        for i in range(0, 3):
            if len(self.inv[i].stack) != 5 and self.inv[i].item_id == item.id:
                self.inv[i].stack.append(item)
                break
            # elif self.inv[i].stack[0] == item and len(self.inv[i].stack) != 5:
            #     self.inv[i].stack.append(item)
            #     break
            else:
                pass
            c = c +1
        if c == 4:
            print('slots full!')
    
    def __str__(self):
        for slot in self.inv:
            try:
                print(f'{slot.item_id}: {slot.stack[0]} #{len(slot.stack)}') #Since each stack can only hold one type of item, we only need to check the first index and get the length to determine what is in the stack
            except:
                pass
    


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
    
    def heal(self, amt, target):
        target.health = target.health + amt

class life_drop:
    def __init__(self):
        self.id = 00 # double zero id is not an inv item, it'll make sense when the drop sys is implmented. i hope
        self.heal_amt = 20

