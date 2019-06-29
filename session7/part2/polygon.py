print('Tôi sẽ giúp bạn vẽ một đa giác.')
a = input('Nhập độ dài cạnh đa giác: ')
while True:
    if a.isdigit():
        c = int(a)
        if c > 0:
            from turtle import *
            for d in range(6):
                forward(c)
                left(60)
            mainloop()
            break
        else:
            a = input('Độ dài cạnh phải lớn hơn 0. Mời nhập lại: ')
    else:
        a = input('Độ dài cạnh phải là một chữ số. Mời nhập lại: ')