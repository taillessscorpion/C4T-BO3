while True:
    a = input('Mời bạn nhập tên: ')
    if a.isalpha():
        print('Xin chào', a)
        break
    else:
        print('Tên của bạn đã chứa số, mời nhập lại.')