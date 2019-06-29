print('ĐĂNG KÍ TÀI KHOẢN')
uname = input('Tên đăng nhập: ')
print('Đã xác nhận thông tin cho tài khoản', uname)
while True:
    password1 = input('Mật khẩu: ')
    pwc = int(len(password1))
    if pwc >= 8:
        if password1.isalpha():
            print('Mật khẩu phải có cả chữ và số. Mời nhập lại.')
        elif password1.isdigit():
            print('Mật khẩu phải có cả chữ và số. Mời nhập lại.')
        elif password1.isalnum():
            password2 = input('Nhập lại mật khẩu: ')
            if password1 < password2:
                print('Mật khẩu không khớp nhau. Đề nghị nhập lại.')
            elif password1 > password2:
                print('Mật khẩu không khớp nhau. Đề nghị nhập lại.')
            else:
                print('Đã xác nhận mật khẩu cho tài khoản', uname)
                break
        else:
            print('Mật khẩu phải có cả chữ và số. Mời nhập lại.')
    else:
        print('Mật khẩu phải dài hơn hoặc bằng 8 kí tự. Mời nhập lại.')
while True:
    email = input('Email: ')
    if email.endswith('.com'):
        if '@' in email:
            print('Đăng kí thành công tài khoản', uname)
            break
        else:
            print('Tài khoản email không tồn tài. Mời kiểm tra lại.')
    else:
        print('Tài khoản email không tồn tài. Mời kiểm tra lại.')