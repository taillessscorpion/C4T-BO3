a = input('Mời bạn nhập một số bất kì: ')
while True:
    if a.isdigit():
        b = int(a) % 2
        if b < 1:
            print('Số', a, 'bạn vừa nhập là số chẵn.')
            break
        else:
            print('Số', a, 'bạn vừa nhập là số lẻ.')
            break
    else:
        a = input('Số bạn vừa nhập không tồn tại. Mời nhập lại: ')