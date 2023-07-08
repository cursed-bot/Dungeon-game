#for setting up items/ inventory

class inventory:
    def __init__(self):
        self.inv = [slot(), slot(), slot()]
    
    def get_item(self, item):
        c = 0
        for i in range(0, 2):
            if len(self.inv[i].stack) == 0 :
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
    
    def clear_slot(self, slot_num):
        self.inv[int(slot_num)].stack.clear()
        print(f'{slot_num} cleared!')
    
"""     def use_item(self, item):
            try:
                self.inv[int(item)].stack[0].use()
                self.inv[int(item)].stack.remove(item)
            except:
                pass """
# to be implemented

class slot:
        def __init__(self):
            self.stack = []
