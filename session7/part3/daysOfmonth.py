year = input('Nhập vào một năm bất kì: ')
while True:
    if year.isdigit():
        y = int(year)
        print('Đã xác nhận năm', y)
        month = input('Nhập tháng mà bạn muốn biết số ngày trong năm:')
        break
    else:
        year = input('Năm mà bạn nhập không tồn tại, năm phải là một số. Mời nhập lại: ')
while True:
    if month.isdigit():
        m = int(month)
        if 1 <= m <= 11:
            import datetime
            day1 = datetime.datetime(y,m+1,1)
            day2 = datetime.datetime(y,m,1)
            d1 = int(day1.strftime('%j'))
            d2 = int(day2.strftime('%j'))
            d = d1 - d2
            print('Tháng', m, 'năm', y, 'có', d, 'ngày.')
            break
        elif 11 < m <= 12:
            import datetime
            day1 = datetime.datetime(y,m,31)
            day2 = datetime.datetime(y,m,1)
            d1 = int(day1.strftime('%j'))
            d2 = int(day2.strftime('%j'))
            d = d1 - d2 + 1
            print('Tháng', m, 'năm', y, 'có', d, 'ngày.')
            break
        else:
            month = input('Tháng mà bạn nhập không tồn tại, tháng là một số nguyên từ 1 đến 12. Mời nhập lại: ')
    else:
        month = input('Tháng mà bạn nhập không tồn tại, tháng là một số nguyên từ 1 đến 12. Mời nhập lại: ')