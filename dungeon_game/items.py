#for setting up items/ inventory

class inventory:
    def __init__(self):
        self.inv = [slot(), slot(), slot()]
    
    def get_item(self, item):
        for i in range(0, 2):
            if len(self.inv[i].stack) == 0 :
                self.inv[i].stack.append(item)
                break
            elif self.inv[i].stack[0] == item and len(self.inv[i].stack) != 5:
                self.inv[i].stack.append(item)
                break
            else:
                pass
        print('No slots left!')
               
class slot:
        def __init__(self):
            self.stack = []
