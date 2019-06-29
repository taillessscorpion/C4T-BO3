print('Tôi sẽ giúp bạn tính bình phương một số nguyên bất kì.')
a = input('Nhập số cần bình phương: ')
while True:
    if a.isdigit():
        b = int(a)
        c = b * b
        print('Số bình phương của', b, 'là', c)
        break
    else:
        a = input('Số bạn vừa nhập không tồn tại. Vui lòng nhập lại: ')


