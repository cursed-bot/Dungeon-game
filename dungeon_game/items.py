#for setting up items/ inventory

class inventory:
    def __init__(self):
        self.inv = [slot(1), slot(2), slot(3), slot(0)]
    
    def get_item(self, item):
        c = 0
        for i in range(0, 2):
            if len(self.inv[i].stack) == 0 and self.inv[i].item_id == item.id:
                self.inv[i].stack.append(item)
                break
            elif self.inv[i].stack[0] == item and len(self.inv[i].stack) != 5:
                self.inv[i].stack.append(item)
                break
            else:
                pass
            c = c +1
        if c == 3:
            print('slots full!')
    
    

class slot:
        def __init__(self, id):
            self.stack = []
            self.item_id = id

    
class test_item:
    def __init__(self):
        self.id = 0
        self.type = 'testing'
        self.actions = {'heal': 20, 'super heal': 100}
    
    def use(self):
        run = 1
        for key, value in self.actions.items():
            print(f'{run}: {key}')
            run = run + 1
        
