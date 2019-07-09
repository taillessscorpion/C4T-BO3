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
w = 0
while w < 2:
    listname = []
    namevalue = input('Nhập tên máy cần mua và số lượng, cách nhau bởi dấu ":". ')
    lennamvalue = len(namevalue)
    listnv = list(namevalue)
    countspace = namevalue.count(' ', 0, lennamvalue)
    for i in range(countspace):
        lennamvalue = len(namevalue)
        locationspace = namevalue.find(' ', 0, lennamvalue)
        listnv.pop(locationspace)
        namevalue = ''.join(listnv)
    countcolon = namevalue.count(':', 0, lennamvalue)
    if countcolon == 1:
        locationcolon = namevalue.find(':', 0, lennamvalue)
        for i in range(locationcolon):
            listname.append(listnv[0])
            listnv.pop(0)
        listnv.pop(0)
        rawname = ''.join(listname)
        name = rawname.upper()
        amount = ''.join(listnv)
        if name.isalpha():
            for i, j in enumerate(computers):
                if name == j['name']:
                    w += 1
                    if amount.isdigit():
                        if 1 <= int(amount) <= j['value']:
                            j['value'] -= int(amount)
                            print('Số lượng máy {} còn lại trong kho sau khi đã mua {} máy là {} máy.'.format(j['name'], amount, j['value']))
                            w += 1
                            break
                        elif int(amount) < 1:
                            print('Bạn không thể mua {} máy {} được. Mời nhập lại số lượng.'.format(amount, j['name']))
                        else:
                            print('Trong kho chỉ còn {}. Mời nhập lại số lượng.'.format(j['value']))
                    else:
                        print('{} không thể là số lượng máy. Mời nhập lại một số.'.format(amount))
                else:
                    if j['name'] == computers[-1]['name']:
                        print('Máy {} không có trong kho. Mời tìm máy khác.'.format(name.lower()))
                    else:
                        pass
        else:
            print('Máy {} không tồn tại. Mời tìm máy khác.'.format(name))
    else:
        print('Không thể xác nhận thông tin. Mời nhập lại.')





