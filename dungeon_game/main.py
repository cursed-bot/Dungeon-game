# A dungon game! I guess
from dungeon_game.rooms import *
from dungeon_game.entities import *
#from dungeon_game.level import *

def main():
    room1 = Room()
    #room2 = Room()
    player = human('player', 5)
    total_e = len(room1.enemies)
    total_d = 0

    while True:
        if player.alive == False:
            print('Game Over!')
            break

        for enemy in room1.enemies:
            match enemy.alive:
                case True:
                    print(f'{enemy.id}: {enemy.species} has {enemy.health} health left')
                case False:
                    if enemy.counted == False:
                        enemy.counted = True
                        total_d = total_d + 1
                    else:
                        continue
        if total_d == total_e:
            print('All enemies defeated!')
            break

        while True:
            turn = 1
            print(f'You have {player.health} life left')
            attack = input('choose a monster to attack: ')
            for enemy in room1.enemies:
                try:
                    if int(attack.strip()) == enemy.id:
                        player.attack(enemy)
                        turn = 0
                        break
                    else:
                        continue
                except:
                    break
            if turn == 0:
                break
            print("not a vaild target, please try again")
        
        for enemy in room1.enemies:
            match enemy.alive:
                case True:
                    match player.alive:
                        case True:
                            enemy.attack(player)
                        case False:
                            continue
                case False:
                    continue

if __name__ == "__main__":
    main()