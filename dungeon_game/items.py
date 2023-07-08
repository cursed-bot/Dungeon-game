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
    


class slot:
        def __init__(self, id, name):
            self.stack = []
            self.item_id = id
            self.user = name

    
class test_item:
    def __init__(self, user):
        self.id = 0
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

