print('Xin chào.')

a = input('Mời nhập một đoạn kí tự: ')
while True:
    if a.isalpha():
        print('Đoạn kí tự của bạn sẽ được chuyển thành viết hoa là:', a.upper())
        break
    else:
        print(a)
        break
