maps = ['-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-','-', '-', '-', '-',]
from random import randint
le = randint(0,15)
while True:
    lk = randint(0,15)
    if lk != le:
        break
    else:
        pass
while True:
    lp = randint(0,15)
    if lp != le and lp != lk:
        break
    else:
        pass
maps[le] = 'E'
maps[lk] = 'K'
maps[lp] = 'P'
P = 0
#KHỞI TẠO MAP
def cannotmoving():
    print('You cannot move over there!')
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
        if P == 1:
            print('You win!!!')
            break
        if P == 0:
            print('You need to pick up the key(s) first.')
    elif lp == lk:
        print("You've just picked up a key!!!")
        P += 1
        lk = 'done'
    move = input('Your move?    ')
    if lp == 0:
        if move == 'w' or move == 'a':
            cannotmoving()
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'd':
            moving(lp,1)
            lp += 1
    elif lp == 3:
        if move == 'w' or move == 'd':
            cannotmoving()
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'a':
            moving(lp,-1)
            lp -= 1
    elif lp == 12:
        if move == 's' or move == 'a':
            cannotmoving()
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 'd':
            moving(lp,1)
            lp += 1
    elif lp == 15:
        if move == 's' or move == 'd':
            cannotmoving()
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 'a':
            moving(lp,-1)
            lp -= 1
    elif lp == 1 or lp == 2:
        if move == 'a':
            moving(lp,-1)
            lp -= 1
        elif move == 'w':
            cannotmoving()
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'd':
            moving(lp,1)
            lp += 1
    elif lp == 4 or lp == 8:
        if move == 'a':
            cannotmoving()
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'd':
            moving(lp,1)
            lp += 1
    elif lp == 7 or lp == 11:
        if move == 'a':
            moving(lp,-1)
            lp -= 1
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'd':
            cannotmoving()
    elif lp == 13 or lp == 14:
        if move == 'a':
            moving(lp,-1)
            lp -= 1
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 's':
            cannotmoving()
        elif move == 'd':
            moving(lp,1)
            lp += 1
    else:
        if move == 'a':
            moving(lp,-1)
            lp -= 1
        elif move == 'w':
            moving(lp,-4)
            lp -= 4
        elif move == 's':
            moving(lp,4)
            lp += 4
        elif move == 'd':
            moving(lp,1)
            lp += 1
    if lp == le:
        maps[le] = 'P'
    else:
        maps[le] = 'E'
    show()
