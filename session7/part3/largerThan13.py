a = input('Mời nhập vào một số bất kì: ')
while True:
    if a.isdigit():
        b = int(a)
        if b < 13:
            print('Số', b, 'bạn vừa nhập có giá trị nhỏ hơn 13.')
            break
        elif b > 13:
            print('Số', b, 'bạn vừa nhập có giá trị lớn hơn 13.')
            break
        else:
            print('Số bạn vừa nhập là', b)
            break
    else:
        a = input('Số bạn vừa nhập không tồn tại. Mời nhập lại: ')