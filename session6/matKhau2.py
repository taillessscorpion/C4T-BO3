while True:
    a = input('Mời bạn nhập mật khẩu: ')
    if a.isalpha():
        print('Mật khẩu không chứa số, mời nhập lại.')
    else:
        if len(a) < 8:
            print('Mật khẩu phải có trên 8 ký tự.')
        else:
            print('Mật khẩu hợp lệ.')
            break