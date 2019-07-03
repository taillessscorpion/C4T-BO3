a = {
    'name': ' Nguyen Van A',
    'age': 50,
    'sex': 'male'
}
while True:
    key = input('Nhập key: ')
    if key in a:
        print(a[key])
        break
    else:
        print('Key {} không tồn tại. Mời nhập lại.'.format(key))