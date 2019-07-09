computers = [{
    'name': 'HP',
    'value': 20,
    'price': 600,
}, {
    'name': 'DELL',
    'value': 50,
    'price': 650,
}, {
    'name': 'MACBOOK',
    'value': 12,
    'price': 12000,
}, {
    'name': 'ASUS',
    'value': 30,
    'price': 400,
}, {
    'name': 'ACER',
    'value': 35,
    'price': 350,
},{
    'name': 'TOSHIBA',
    'value': 10,
    'price': 600,
},{
    'name': 'FUJISTU',
    'value': 15,
    'price': 900,
}, {
    'name': 'ALIENWARE',
    'value': 5,
    'price': 1000,
}]
w1 = 0
while w1 < 1:
    name = input('Nhập tên máy cần mua: ').upper()
    if name.isalpha():
        for i, j in enumerate(computers):
            if name == j['name']:
                w1 = 1
                break
            else:
                if j['name'] == computers[-1]['name']:
                    print('Máy {} không có trong kho. Mời tìm máy khác.'.format(name.lower()))
                else:
                    pass
    else:
        print('Máy {} không tồn tại. Mời tìm máy khác.'.format(name))
w2 = 0
while w2 < 1:
    amount = input('Nhập số lượng máy cần mua: ')
    if amount.isdigit():
        if 1 <= int(amount) <= j['value']:
            j['value'] -= int(amount)
            print('Số lượng máy {} còn lại trong kho sau khi đã mua {} máy là {} máy.'.format(j['name'], amount, j['value']))
            w = 1
            break
        elif int(amount) < 1:
            print('Bạn không thể mua {} máy {} được. Mời nhập lại số lượng.'.format(amount, j['name']))
        else:
            print('Trong kho chỉ còn {}. Mời nhập lại số lượng.'.format(j['value']))
    else:
        print('{} không thể là số lượng máy. Mời nhập lại một số.'.format(amount))