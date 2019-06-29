print('XIN CHÀO.')
while True:
    first = input('Mời nhập họ của bạn tại đây: ')
    if first.isalpha():
        break
    else:
        print('Họ của bạn không hợp lệ! Mời nhập lại.')
while True:
    last = input('Mời nhập tên của bạn tại đây: ')
    if last.isalpha():
        break
    else:
        print('Tên của bạn không hợp lệ! Mời nhập lại.')
print('Xin chào,', first, last)