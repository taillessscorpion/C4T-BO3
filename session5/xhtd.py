m = int(input('Nhập một tháng bất kì trong năm: '))
if m <= 0:
    print('Tháng bạn nhập không tồn tại.')
elif m < 4:
    print('Tháng', m, 'là mùa xuân.')
elif m < 7:
    print('Tháng', m, 'là mùa hạ.')
elif m < 10:
    print('Tháng', m, 'là mùa thu.')
elif m < 13:
    print('Tháng', m, 'là mùa đông.')
else:
    print('Tháng bạn nhập không tồn tại.')
