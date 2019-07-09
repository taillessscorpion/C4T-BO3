computers = [{
    'name': 'HP',
    'value': 20
}, {
    'name': 'DELL',
    'value': 50
}, {
    'name': 'MACBOOK',
    'value': 12
}, {
    'name': 'ASUS',
    'value': 30
}]
for i, j in enumerate(computers):
    if j['name'] == 'MACBOOK':
        print('Số lượng {} trong kho là {}.'.format(j['name'],j['value']))