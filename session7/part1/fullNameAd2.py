print('XIN CHÀO.')
while True:
    namecount = input('Họ và tên của bạn có bao nhiêu chữ: ')
    if namecount.isdigit():
        nc = int(namecount)
        if nc > 2:
            print('Đã xác nhận tên của bạn có {} chữ.'.format(nc))
            w = 0
            break
        elif nc == 2:
            print('Đã xác nhận tên của bạn có {} chữ.'.format(nc))
            w = 1
            break
        else:
            print('Tên của bạn phải có ít nhất 2 chữ. Mời nhập lại')
    else:
        print('Tên của bạn không thể có', namecount, 'chữ.')
while True:
    first = input('Mời nhập họ của bạn tại đây: ')
    if first.isalpha():
        f = list(first)
        f[0] = f[0].upper()
        first = ''.join(f)
        print('Đã xác nhận họ của bạn là {}.'.format(first))
        break
    else:
        print('Họ của bạn không hợp lệ! Mời nhập lại.')
print('CHÚ Ý: Nếu tên lót của bạn có trên 2 chữ, hãy ngăn cách bằng khoảng trống.')
while w < 1:
    middle = input('Mời nhập tên lót của bạn tại đây: ')
    if middle.isprint():
        print('test')
        w = 1
    else:
        print('Tên lót của bạn không hợp lệ! Mời nhập lại.')
while True:
    last = input('Mời nhập tên của bạn tại đây: ')
    if last.isalpha():
        break
    else:
        print('Tên của bạn không hợp lệ! Mời nhập lại.')
print('Xin chào,', first, last)