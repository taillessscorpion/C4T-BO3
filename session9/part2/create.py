clist = ['red', 'blue', 'green']
llist = len(clist)
while True:
    position = input('Nhập vị trí: ')
    if position.isdigit():
        p = int(position)
        if p <= llist-1:
            p = int(position)
            print(clist[p-1])
            break
        else:
            print('Vị trí {} nằm ngoài danh sách. Vị trí là một số thuộc từ 1 đến {}'.format(p, llist))
    else:
        print('Vị trí {} không tồn tại. Vị trí phải là số. Mời nhập lại.'.format(position))