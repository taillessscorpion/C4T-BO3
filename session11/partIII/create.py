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
computers.append({
    'name': 'FUJISTU',
    'value': 15,
})
computers.append({
    'name': 'ALIENWARE',
    'value': 5,
})
totalvalue = 0
for i, j in enumerate(computers):
    totalvalue += j['value']
print('Tổng máy tính trong kho là {} chiếc.'.format(totalvalue))