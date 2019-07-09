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
w=0
while w < 1:
    name = input('Nhập tên máy để xem giá: ').upper()
    if name.isalpha():
        for i, j in enumerate(computers):
            if name == j['name']:
                print('Giá của máy {} là {}.'.format(j['name'], j['price']))
                w=1
                break
            else:
                if j['name'] == computers[-1]['name']:
                    print('Máy {} không có trong kho. Mời tìm máy khác.'.format(name.lower()))
                else:
                    pass
    else:
        print('Máy {} không tồn tại. Mời tìm máy khác.'.format(name))

