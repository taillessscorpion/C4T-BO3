print('Xin chào, tôi sẽ giúp bạn vẽ một hình tròn bất kì.')
r = input('Mời bạn nhập giá trị bán kính: ')
while True:
    if r.isdigit():
        a = int(r)
        from turtle import *
        circle(a)
        mainloop()
        break
    else:
        r = input('Bán kính bạn vừa nhập vào không tồn tại. Mời nhập lại: ')
