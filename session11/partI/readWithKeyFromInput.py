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
w = 0
while w < 1:
    print(w)
    name = input('Nhập tên máy tính để xem số lượng: ')
    if name.isalpha():
        Capname = name.upper()
        for i, j in enumerate(computers):
            if Capname != j['name']:
                if j == computers[-1]:
                    print('Không có bất cứ máy {} nào trong kho, mời tìm kiếm loại máy khác'.format(name))
                else:
                    pass
            elif Capname == j['name']:
                print('Số lượng máy tính {} còn lại trong kho là {} chiếc.'.format(j['name'],j['value']))
                w += 2
                break

    else:
        print('Máy {} không tồn tại trong kho, mời tìm kiếm loại máy khác.'.format(name))
