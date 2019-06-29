print('XIN CHÀO.')
while True:
    namecount = input('Họ và tên của bạn có bao nhiêu chữ: ')
    if namecount.isdigit():
        nc = int(namecount)
        if nc > 2:
            print('Đã xác nhận tên của bạn có {} chữ.'.format(nc))
            w = 0
            break
        elif nc == 2:
            print('Đã xác nhận tên của bạn có {} chữ.'.format(nc))
            w = 1
            break
        else:
            print('Tên của bạn phải có ít nhất 2 chữ. Mời nhập lại')
    else:
        print('Tên của bạn không thể có', namecount, 'chữ.')
while True:
    first = input('Mời nhập họ của bạn tại đây: ')
    if first.isalpha():
        f = list(first)
        f[0] = f[0].upper()
        first = ''.join(f)
        print('Đã xác nhận họ của bạn là {}.'.format(first))
        break
    else:
        print('Họ của bạn không hợp lệ! Mời nhập lại.')
if nc > 2:
    print('CHÚ Ý: Hãy ngăn cách tên lót của bạn bằng khoảng trống.')
else:
    pass
while w < 1:
    middle = input('Mời nhập tên lót của bạn tại đây: ')
    cmid = middle
    checkmid = list(cmid)
    lenmid = len(cmid)    
    lospace = cmid.find(' ', 0, lenmid)
    cospace = cmid.count(' ', 0, lenmid)
    if lospace == 0:
        print('Tên lót của bạn không thể bắt đầu với khoảng trống. Vui lòng nhập lại.')
    else:
        for checkspace in range(cospace):
            checkmid = list(cmid)
            lenmid = len(cmid)
            lospace = cmid.find(' ', 0, lenmid)
            checkmid.pop(lospace)
            cmid = ''.join(checkmid)
        if cmid.isalpha():
            if cospace == nc - 3:
                listmid = list(middle)
                donemiddle = []
                lenmid = len(middle)    
                cospace = middle.count(' ', 0, lenmid) 
                lospace = middle.find(' ', 0, lenmid)
                if cospace == 0:
                    listmid[0] = listmid[0].upper()
                    middle = ''.join(listmid)
                else:
                    for i in range(cospace):    
                        lenmid = len(middle)    
                        cospace = middle.count(' ', 0, lenmid) 
                        lospace = middle.find(' ', 0, lenmid)
                        midx = listmid[0:lospace]
                        midx[0] = midx[0].upper()
                        midy = ''.join(midx)
                        donemiddle.append(midy)
                        donemiddle.append(' ')
                        for j in range(lospace+1):
                            listmid.pop(0)
                            listmid[0] = listmid[0].upper()
                            middle = ''.join(listmid)
                    donemiddle.append(middle)
                    middle = ''.join(donemiddle)
                print('Đã xác nhận tên lót của bạn là {}.'.format(middle))
                w = 1
            elif cospace < nc - 3:
                print('Bạn nhập tên lót thiếu {} chữ so với khai báo tên lót có {} chữ của bạn.'.format(nc-3-cospace,nc-2))
            elif cospace > nc - 3:
                print('Bạn nhập tên lót thừa {} chữ so với khai báo tên lót có {} chữ của bạn.'.format(cospace+3-nc,nc-2))
        else:
            print('Tên lót của bạn không hợp lệ! Mời nhập lại.')
while True:
    last = input('Mời nhập tên của bạn tại đây: ')
    if last.isalpha():
        l = list(last)
        l[0] = l[0].upper()
        last = ''.join(l)
        print('Đã xác nhận họ của bạn là {}.'.format(last))
        break
    else:
        print('Tên của bạn không hợp lệ! Mời nhập lại.')
if nc == 2:
    print('Xin chào, {} {}.'.format(first, last))
elif nc > 2:
    print('Xin chào, {} {} {}.'.format(first, middle, last))