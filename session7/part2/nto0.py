n = input('Mời nhập vào một số bất kì lớn hơn 0: ')
while True:
    if n.isdigit():
        a = int(n)
        if a > 0:
            cl = a % 2
            if cl < 1:
                for c in range(a-1,0,-2):
                    print(c)
                break
            else:
                for l in range(a,0,-2):
                    print(l)
                break
        else:
            n = input('Số bạn nhập phải lớn hơn 0. Mời nhập lại: ')
    else:
        n = input('Số bạn nhập vào không hợp lệ. Mời nhập lại: ')