while True:
    a = input('Mời bạn nhập vào một số bất kì: ')
    if a.isdigit():
        print('Số', a, 'có', len(a), 'chữ số.')
        break
    else:
        print('Mời bạn nhập SỐ.')