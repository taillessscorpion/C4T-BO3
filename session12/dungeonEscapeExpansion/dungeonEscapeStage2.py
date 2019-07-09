maps = ['-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-','-', '-', '-', '-',]
from random import randint
le = randint(0,15)
while True:
    lk1 = randint(0,15)
    if lk1 != le:
        break
while True:
    lk2 = randint(0,15)
    if lk2 != le and lk2 != lk1:
        break
while True:
    lp = randint(0,15)
    if lp != le and lp != lk1 and lp != lk2:
        break
while True:
    lw1 = randint(0,15)
    if lw1 != le and lw1 != lk1 and lw1 != lp and lw1 != lk2:
        break
while True:
    lw2 = randint(0,15)
    if lw2 != le and lw2 != lk1 and lw2 != lp and lw2 != lw1 and lw2 != lk2:
        lw = lw1 + lw2
        if lw % 2 == 1:
            break
maps[le] = 'E'
maps[lk1] = 'K'
maps[lk2] = 'K'
maps[lp] = 'P'
maps[lw1] = 'W'
maps[lw2] = 'W'
P = 0
def cannotmoving():
    print('You cannot move over there!')
def cannotthrough():
    print('You cannot move through the wall.')
def moving(a,b):
    maps[a] = '-'
    maps[a+b] = 'P'
def show():
    print(*maps[0:4], sep = '  ')
    print(*maps[4:8], sep = '  ')
    print(*maps[8:12], sep = '  ')
    print(*maps[12:16], sep = '  ')
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
    move = input('Your move?    ')
    print(P)
    if lp == 0:
        if move == 'w' or move == 'a':
            cannotmoving()
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 3:
        if move == 'w' or move == 'd':
            cannotmoving()
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
        elif move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
    elif lp == 12:
        if move == 's' or move == 'a':
            cannotmoving()
        elif move == 'w':
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 15:
        if move == 's' or move == 'd':
            cannotmoving()
        elif move == 'w':
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
        elif move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
    elif lp == 1 or lp == 2:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            cannotmoving()
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 4 or lp == 8:
        if move == 'a':
            cannotmoving()
        elif move == 'w':
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
        elif move == 'd':
            if lp+1 == lw1 or lp+1 == lw2:
                cannotthrough()
            else:
                moving(lp,1)
                lp += 1
    elif lp == 7 or lp == 11:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
        elif move == 'd':
            cannotmoving()
    elif lp == 13 or lp == 14:
        if move == 'a':
            if lp-1 == lw1 or lp-1 == lw2:
                cannotthrough()
            else:
                moving(lp,-1)
                lp -= 1
        elif move == 'w':
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
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
            if lp-4 == lw1 or lp-4 == lw2:
                cannotthrough()
            else:
                moving(lp,-4)
                lp -= 4
        elif move == 's':
            if lp+4 == lw1 or lp+4 == lw2:
                cannotthrough()
            else:
                moving(lp,4)
                lp += 4
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
    show()
