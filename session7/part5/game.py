from random import randint
p = 0
o = 0
while o < 1:
    a = randint(0,50)
    b = randint(0,50)
    c = randint(0,1)
    ba = randint(0,1)
    if c == 0:
        c = a - b
        if ba == 0:
            d = randint(c-3,c+3)
            print(a,'-', b, '=', d)
            if d == c:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    elif r.isalpha() and r == 's':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
            else:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    elif r.isalpha() and r == 's':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
        if ba == 1:
            d = c
            print(a,'-', b, '=', d)
            if d == c:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    elif r.isalpha() and r == 's':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
            else:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    elif r.isalpha() and r == 's':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
    elif c == 1:
        c = a + b
        if ba == 0:
            d = randint(c-3,c+3)
            print(a,'+', b, '=', d)
            if d == c:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    elif r.isalpha() and r == 's':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
            else:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    elif r.isalpha() and r == 's':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
        if ba == 1:
            d = c
            print(a,'+', b, '=', d)
            if d == c:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    elif r.isalpha() and r == 's':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')
            else:
                while True:
                    r = input('nếu đúng nhấn d, nếu sai nhấn s: ')
                    if r.isalpha() and r == 'd':
                        print('Bạn đã dừng cuộc chơi với số điểm là', p, 'điểm.')
                        o = 1
                        break
                    elif r.isalpha() and r == 's':
                        p += 1
                        print('Điểm của bạn là', p, 'điểm.')
                        break
                    else:
                        print('Không xác nhận được câu trả lời.')

