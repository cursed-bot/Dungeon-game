from random import randint
from dungeon_game.entities import slime, goblin

rooms = ["hallway", "normal", "dungeon", "armoury"]
rsize = ["small", "medium", "large"]


######################
### room gen/setup ###
######################
class Room:
    def __init__(self, *args):
        try: # Try to set room config settings using values in the order of: room type, room size, and the player
            self.room_type = rooms[args[0]]
            self.size = rsize[args[1]]
            self.player = args[2]
            self.__room_config()
        except: # If that fails, randomize the room type and size, but set the player as the player is ALWAYS passed when a Room is created 
            print('error parsing args, randomizing...')
            self.room_type = rooms[randint(0, 3)]
            self.size = rsize[0]
            self.player = args[0]
            self.__room_config() # makes a room based on the randomly picked indexes
            #self.__test_room() #for testing 

    def __room_config(self): # I LOVE match case!!!!
        match self.size:
            case 'small':
                match self.room_type:
                    case 'normal':
                        self.m1 = slime(1)
                        self.m2 = slime(2)
                        self.enemies = [self.m1, self.m2]
                    case 'hallway':
                        self.m1 = slime(1)
                        self.enemies = [self.m1]
                    case 'armoury':
                        self.m1 = slime(1)
                        self.m2 = goblin(2)
                        self.enemies = [self.m1, self.m2]
                    case 'dungeon':
                        self.m1 = goblin(1)
                        self.m2 = goblin(2)
                        self.m3 = goblin(3)
                        self.enemies = [self.m1, self.m2, self.m3]
                    case '_':
                        print('Something went wrong!')
            # case 'medium':
            #     match self.room_type:
            #         case 'normal':
            #             print('5')
            #         case 'hallway':
            #             print('6')
            #         case 'armoury':
            #             print('7')
            #         case 'dungeon':
            #             print('8')
            #         case '_':
            #             pass
            # case 'large':
            #     match self.room_type:
            #         case 'normal':
            #             print('9')
            #         case 'hallway':
            #             print('10')
            #         case 'armoury':
            #             print('11')
            #         case 'dungeon':
            #             print('12')
            #         case '_':
            #             pass
            # case '_':
            #     pass

    def __test_room(self):
        self.m1 = slime()
        self.m2 = goblin()
        self.enemies = [self.m1, self.m2]