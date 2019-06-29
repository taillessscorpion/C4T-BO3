print('ĐĂNG KÍ TÀI KHOẢN')
uname = input('Tên đăng nhập: ')
print('Đã xác nhận thông tin cho tài khoản', uname)
while True:
    password1 = str(input('Mật khẩu: '))
    password2 = str(input('Nhập lại mật khẩu: '))
    if password1 < password2:
        print('Mật khẩu không khớp nhau. Đề nghị nhập lại.')
    elif password1 > password2:
        print('Mật khẩu không khớp nhau. Đề nghị nhập lại.')
    else:
        print('Đã xác nhận mật khẩu cho tài khoản', uname)
        break
email = input('Email: ')
print('Đăng kí thành công tài khoản', uname)
