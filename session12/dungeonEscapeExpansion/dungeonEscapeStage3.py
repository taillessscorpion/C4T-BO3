maps = ['-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-','-', '-', '-', '-', '-','-', '-', '-', '-','-', '-', '-', '-']
characters = [{
    'name': 'Monster',
    'hp': 200,
    'strength': 10,
    'damage': 5,
    'armor': 50,
    'defense': 35,
}, {
    'name': 'Player',
    'hp': 75,
    'strength': 10,
    'damage': 20,
    'armor': 10,
    'defense': 10,
}]
from random import randint
le = randint(0,24)
while True:
    lk1 = randint(0,24)
    if lk1 != le:
        break
while True:
    lk2 = randint(0,24)
    if lk2 != le and lk2 != lk1:
        break
while True:
    lp = randint(0,24)
    if lp != le and lp != lk1 and lp != lk2:
        break
while True:
    lw1 = randint(0,24)
    if lw1 != le and lw1 != lk1 and lw1 != lp and lw1 != lk2:
        break
while True:
    lw2 = randint(0,24)
    if lw2 != le and lw2 != lk1 and lw2 != lp and lw2 != lw1 and lw2 != lk2:
        lw = lw1 + lw2
        if lw % 2 == 1:
            break
while True:
    lm = randint(0,24)
    if lm != le and lm != lk1 and lm != lp and lm != lw1 and lm != lk2 and lm != lw2:
        break
maps[le] = 'E'
maps[lk1] = 'K'
maps[lk2] = 'K'
maps[lp] = 'P'
maps[lw1] = 'W'
maps[lw2] = 'W'
maps[lm] = 'M'
P = 0
def cannotmoving():
    print('You cannot move over there!')
def cannotthrough():
    print('You cannot move through the wall.')
def moving(a,b):
    maps[a] = '-'
    maps[a+b] = 'P'
def show():
    print(*maps[0:5], sep = '  ')
    print(*maps[5:10], sep = '  ')
    print(*maps[10:15], sep = '  ')
    print(*maps[15:20], sep = '  ')
    print(*maps[20:25], sep = '  ')
def combat():
    print('{}        {}          {}           {}          {}         {}'.format(characters[0]['name'],characters[0]['hp'],characters[0]['strength'],characters[0]['damage'],characters[0]['armor'],characters[0]['defense']))
    print('[ V S ]      [ H P ]    [ S T R ]   [ D M G ]   [ A M R ]   [ D E F ]')
    print('{}         {}          {}           {}          {}         {}'.format(characters[1]['name'],characters[1]['hp'],characters[1]['strength'],characters[1]['damage'],characters[1]['armor'],characters[1]['defense']))
show()
while True:
    if lp == le:
        if P == 2:
            print('You win!!!')
            break
        else:
            print('You need to pick up enough key(s) first.')
    elif lp == lk1:
        print("You've just picked up a key!!!")
        P += 1
        lk1 = 'done'
    elif lp == lk2:
        print("You've just picked up a key!!!")
        P += 1
        lk2 = 'done'
    elif lp == lm:
        print("You're next to the Monster, try to Fight, Run or Defense.")
        while True:
            if characters[0]['hp'] <= 0:
                print("You've just killed Monster!")
                maps[lm] = 'P'
                lm = 'done'
                show()
                break
            elif characters[1]['hp'] <= 0:
                maps[lp] = 'M'
                show()
                print("You're dead!")
                break
            combat()
            action = input('Your action?    ')
            if action == 'r':
                lucky = randint(0,1)
                if lucky == 1:
                    print('You run far away from Monster.')
                    maps[lp] = 'P'
                    show()
                    break
                else:
                    if characters[0]['strength'] - characters[1]['armor'] >= 0:
                        print('Monster catch you!! Monster attacks you a hit {} damage.'.format(characters[0]['strength'] - characters[1]['armor'] + characters[0]['damage']))
                        characters[1]['hp'] -= characters[0]['strength'] + characters[0]['damage'] - characters[1]['armor']
                        characters[1]['armor'] -= 1
                    else:
                        print('Monster catch you!! Monster attacks you a hit {} damage.'.format(characters[0]['damage']))
                        characters[1]['hp'] -= characters[0]['damage']
            elif action == 'd':
                if characters[0]['strength'] - characters[1]['armor'] >= 0 and characters[1]['armor'] > 0 :
                    if characters[0]['damage'] - characters[1]['defense'] > 0:
                        print("You was defensing, but you took {} damage from Monster".format(characters[0]['strength'] + characters[0]['damage'] - characters[1]['armor'] - characters[1]['defense']))
                        characters[1]['hp'] -= characters[0]['strength'] + characters[0]['damage'] - characters[1]['armor'] - characters[1]['defense']
                        characters[1]['armor'] -= 1
                    elif characters[0]['damage'] - characters[1]['defense'] == 0:
                        print("The monster attacked, you're still fine but your armor is damaged.")
                        characters[1]['armor'] -= 1
                    else:
                        characters[0]['hp'] -= characters[1]['defense'] - characters[0]['damage']
                        print('You even payback Monster {} damage but your armor is damaged.'.format(characters[1]['defense'] - characters[0]['damage']))
                        characters[1]['armor'] -= 1
                else:
                    if characters[0]['damage'] - characters[1]['defense'] > 0:
                        print("You was defensing, but you took {} damage from Monster".format(characters[0]['damage'] - characters[1]['defense']))
                        characters[1]['hp'] -= characters[0]['damage'] - characters[1]['defense']
                    elif characters[0]['damage'] - characters[1]['defense'] == 0:
                        print("The monster attacked, you're very well.")
                    else:
                        characters[0]['hp'] -= characters[1]['defense'] - characters[0]['damage']
                        print('You even payback Monster {} damage.'.format(characters[1]['defense'] - characters[0]['damage']))
            elif action == 'f':
                if characters[1]['strength'] - characters[0]['armor'] >= 0 and characters[0]['armor'] > 0:
                    characters[0]['hp'] -= characters[1]['strength'] + characters[1]['damage'] - characters[0]['armor']
                    print('You attacked Monster {} damage.'.format(characters[1]['strength'] + characters[1]['damage'] - characters[0]['armor']))
                    characters[0]['armor'] -= 1
                else:
                    characters[0]['hp'] -= + characters[1]['damage']
                    print('You attacked Monster {} damage.'.format(characters[1]['damage']))
                if characters[0]['strength'] - characters[1]['armor'] >= 0 and characters[1]['armor'] > 0:
                    characters[1]['hp'] -= characters[0]['strength'] + characters[0]['damage'] - characters[1]['armor']
                    print('Monster attacked you {} damage.'.format(characters[0]['strength'] + characters[0]['damage'] - characters[1]['armor']))
                    characters[1]['armor'] -= 1
                else:
                    characters[1]['hp'] -= + characters[0]['damage']
                    print('Monster attacked you {} damage.'.format(characters[0]['damage']))
    if characters[1]['hp'] <= 0:
        break
    move = input('Your move?    ')
    if lp == 0:
        if move == 'w' or move == 'a':
            cannotmoving()
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 4:
        if move == 'w' or move == 'd':
            cannotmoving()
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
    elif lp == 20:
        if move == 's' or move == 'a':
            cannotmoving()
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 24:
        if move == 's' or move == 'd':
            cannotmoving()
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
    elif lp == 1 or lp == 2 or lp == 3:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            cannotmoving()
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 5 or lp == 10 or lp == 15:
        if move == 'a':
            cannotmoving()
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 9 or lp == 14 or lp == 19:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'd':
            cannotmoving()
    elif lp == 21 or lp == 22 or lp == 23:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 's':
            cannotmoving()
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    else:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            if lp-5 == lw1 or lp-5 == lw2:
                cannotthrough()
            else:
                moving(lp,-5)
                lp -= 5
        elif move == 's':
            if lp+5 == lw1 or lp+5 == lw2:
                cannotthrough()
            else:
                moving(lp,5)
                lp += 5
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    if lp == le:
        maps[le] = 'P'
    else:
        maps[le] = 'E'
    if characters[0]['hp'] > 0:
        maps[lm] = 'M'
    show()
