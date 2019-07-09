computers = [{
    'name': 'HP',
    'value': 20,
}, {
    'name': 'DELL',
    'value': 50,
}, {
    'name': 'MACBOOK',
    'value': 12,
}, {
    'name': 'ASUS',
    'value': 30,
}]
totalvalue = 0
for i, j in enumerate(computers):
    totalvalue += j['value']
print('Tổng máy tính trong kho là {} chiếc.'.format(totalvalue))