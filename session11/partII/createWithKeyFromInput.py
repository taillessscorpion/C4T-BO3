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
newCom = {
    'name': '',
    'value': 0,
}
while True:
    name = input('Nhập tên máy tính: ')
    if name.isalpha():
        newCom['name'] = name.upper()
        break
    else:
        print('Tên máy tính không hợp lệ. Mời nhập lại.')
while True:
    value = input('Nhập số lượng máy tính: ')
    if value.isdigit():
        newCom['value'] = value
        break
    else:
        print('Không thể chứa {} chiếc máy tính. Mời nhập lại một số tồn tại.'.format(value))
computers.append(newCom)
for i, j in enumerate(computers):
    print('Có {} chiếc {} trong kho.'.format(j['value'],j['name']))