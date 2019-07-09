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
totalPrice = 0
for i, j in enumerate(computers):
    j['total'] = j['value'] * j['price']
    totalPrice += j['total']
print('Tổng giá trị các máy trong kho là {}'.format(totalPrice))