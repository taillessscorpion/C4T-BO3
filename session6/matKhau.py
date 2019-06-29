while True:
    a = input('Mời bạn nhập mật khẩu: ')
    if a.isalpha():
        print('Mật khẩu không chứa số, mời nhập lại.')
    else:
        print('Mật khẩu hợp lệ.')
        break

