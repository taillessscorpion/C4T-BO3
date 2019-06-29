n = input('Mời nhập vào một số bất kì lớn hơn 0: ')
while True:
    if n.isdigit():
        a = int(n)
        if a > 0:
            for b in range(a+1):
                print(b)
            break
        else:
            n = input('Số bạn nhập phải lớn hơn 0. Mời nhập lại: ')
    else:
        n = input('Số bạn nhập vào không hợp lệ. Mời nhập lại: ')