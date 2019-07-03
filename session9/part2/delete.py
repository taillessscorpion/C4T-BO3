clist = ['red', 'blue', 'green']
llist = len(clist)
print('Dánh sách màu:')
for i, j in enumerate(clist):
    print('{}. {}.'.format(i+1, j))
while True:
    deLete = input('Bạn muốn xóa phần: ')
    if deLete.isdigit():
        denum = int(deLete)
        if denum <= llist:
            clist.pop(denum-1)
            break
        else:
            print('Vị trí {} mà bạn nhập nằm ngoài danh sách. Vị trí thuộc danh sách từ 1 đến {}'.format(deLete, llist))
    if deLete.isalpha():
        if deLete in clist:
            clist.remove(deLete)
            break
        else:
            print('Nội dung "{}" mà bạn nhập nằm ngoài danh sách. Mời nhập lại'.format(deLete))
print('Dánh sách màu đã thay đổi:')
for i, j in enumerate(clist):
    print('{}. {}.'.format(i+1, j))

