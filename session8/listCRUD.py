list1 = []
print('Hãy chọn thao tác cần thực hiện')
print('Để thêm nội dung vào danh sách chọn 1.')
print('Để đọc danh sách chọn 2.')
print('Để thay đổi nội dung danh sách chọn 3.')
print('Để xóa nội dung khỏi danh sách chọn 4.')
print('Để đóng chương trình chọn 5.')
while True:
    llist = len(list1)
    print('BẢNG CHÍNH')
    do = input('Mời chọn thao tác: ')
    if do.isdigit():
        Do = int(do)
        if 1 <= Do <= 5: #Do
            if Do == 1:     #1
                print('THÊM NỘI DUNG')
                add = input('Mời nhập nội dung cần thêm: ')
                list1.append(add)
                print('Đã thêm {} vào danh sách thành công.'.format(add))
            elif Do == 2:   #2
                print('XEM DANH SÁCH')
                if llist >= 1:
                    for i, j in enumerate(list1):
                        print('{}. {}.'.format(i+1, j))
                else:
                    print('Danh sách trống. Mời chọn tháo tác khác.')
            elif Do == 3:   #3
                print('THAY ĐỔI NỘI DUNG')
                w1 = 0
                while w1<1:
                    if llist >= 1:
                        rp = input('Chọn vị trí thay đổi nội dung: ')
                        if rp.isdigit():
                            Rp = int(rp)
                            if 0 <= Rp <= llist + 1:
                                new = input('Nhập nội dung mới: ')
                                list1[Rp-1] = new
                                print('Đã thay đổi nội dung {} vào vị trí số {}'.format(new, Rp))
                                w1 = 1
                            else:
                                print('Vị trí {} không nằm trong danh sách. Danh sách có vị trí từ 1 đến {}'.format(Rp, llist+1))
                        else:
                            print('Vị trí {} không phải là số. Mời nhập lại.'.format(rp))
                    else:
                        print('Xin lỗi. Danh sách trống, bạn không thể thay đổi nội dung. Mời chọn thao tác khác.')
                        w1 = 1
            elif Do == 4:   #4
                print('XÓA NỘI DUNG')
                w2 = 0
                while w2 < 1:
                    if llist >= 1:
                        ifr = input('Nếu bạn muốn xóa theo vị trí, nhập 1. Nếu bạn muốn xóa theo nội dung, nhập 2: ')
                        if ifr.isdigit():
                            IfR = int(ifr)
                            w21 = 0
                            while w21 < 1:
                                if IfR == 1:
                                    lr = input('Nhập vị trí mà bạn muốn xóa: ')
                                    if lr.isdigit():
                                        Lr = int(lr)                       
                                        if 1 <= Lr <= llist:
                                            list1.pop(Lr-1)
                                            print('Đã xóa vị trí {} khỏi danh sách'.format(Lr))
                                            w21 = 1
                                            w2 = 1
                                        else:
                                            print('Vị trí {} không tồn trại trong danh sách. Mời chọn vị trí từ 1 đến {}.'.format(Lr,llist))
                                            rdo = input('Để nhập lại vị trí, nhập 1. Để xóa theo nội dung, nhập 2:')
                                            if rdo.isdigit():
                                                IfR = int(rdo)
                                            else:
                                                ifr = rdo
                                    else:
                                        print('Vị trí {} không tồn tại. Mời nhập lại.'.format(lr))
                                elif IfR == 2:
                                    cr = input('Nhập nội dung mà bạn muốn xóa: ')
                                    if cr in list1:
                                        list1.remove(cr)
                                        print('Đã xóa {} khỏi danh sách.'.format(cr))
                                        w21 = 1
                                        w2 = 1
                                    else:
                                        print('Nội dung {} không tồn tại trong danh sách. Không thể xóa.'.format(cr))
                                        rdo = input('Để nhập lại nội dung, nhập 1. Để xóa theo vị trí, nhập 2: ')
                                        if rdo.isdigit():
                                            Rdo = int(rdo)
                                            if Rdo == 1:
                                                IfR = 2
                                            elif Rdo == 2:
                                                IfR = 1
                                            else:
                                                IfR = Rdo    
                                        else:
                                            ifr = rdo
                                else:
                                    print('Thao tác {} không tồn tại. Mời nhập lại.'.format(IfR))
                                    w21 = 1
                        else:
                            print('Bạn đã nhập sai. Mời nhập lại.')
                            w2 = 1
                    else:
                        print('Xin lỗi. Danh sách trống, bạn không thể xóa. Mời chọn thao tác khác.')
                        w2 = 1
            elif Do == 5:   #5
                print('Đóng chương trình.')
                break
        else:
            print('Thao tác {} không tồn tại. Mời nhập lại'.format(Do))
    else:
        print('Không thực hiện được thao tác {}. Mời nhập lại thao tác'.format(do))