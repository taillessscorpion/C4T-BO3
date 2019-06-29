print('Tôi sẽ giúp bạn vẽ một đa giác.')
a = input('Nhập độ dài cạnh đa giác: ')
while True:
    if a.isdigit():
        aint = int(a)
        if aint > 0:
            print('Đã xác nhận độ dài đa giác bằng {}'.format(a))
            break
        else:
            a = input('Độ dài cạnh phải lớn hơn 0. Mời nhập lại: ')
    else:
        a = input('Độ dài cạnh phải là một chữ số. Mời nhập lại: ')
b = input('Nhập số cạnh của đa giác: ')
while True:
    if b.isdigit():
        bint = int(b)
        if bint >= 3:
            print('Đã xác nhận đa giác có {} cạnh.'.format(b))
            break
        else:
            b = input('Đa giác phải có ít nhất 3 cạnh. Mời nhập lại: ')
    else:
        b = input('Số cạnh của đa giác phải là một chữ số. Mời nhập lại: ')
c = 360 / bint
from turtle import *
speed(-1)
color('white')
right(90)
forward(300)
right(90)
forward(300)
left(180)
color('black')
for d in range(bint):
    forward(aint)
    left(c)
mainloop()