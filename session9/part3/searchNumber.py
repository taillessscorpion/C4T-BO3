#Phần này là mình cố tình cho các phần tử của list là string
#và mình chuyển các phần tử của list thành int.
numberList = ['14', '54', '92', '9', '-4', '-49']
strlist = ''.join(numberList)
llist = len(numberList)
string = ''
newList = []
for i in range(llist):
    string = ''.join(numberList[i])
    intlist = int(string)
    newList.append(intlist)
#Phần này hơi dài, chủ yếu là thêm phần kiểm soát xem người dùng có
#nhập chữ vào hay không. Mặc dù mentor đã hướng dẫn, nhưng mình vẫn
#muốn thử tìm ra cách kiểm soát phần này.
while True:
    findnumber = input('Nhập số cần tìm: ')
    if findnumber.isalpha() or findnumber.isspace():
        print('Số {} không tồn tại. Mời nhập lại.'.format(findnumber))
    else:
        for i, j in enumerate(newList,1):
            if int(findnumber) == j:
                a = i
                b = j
                c = 1
                break
            else:
                c = 0
        if c == 1:
            print('Đã tìm thấy {} tại vị trí {}.'.format(b, a))
            break
        else:
            print('Không tìm thấy số {} trong dãy. Mời nhập lại'.format(findnumber))


# while True:
#     findnumber = int(input('Nhập số cần tìm: '))
#     if findnumber in numberList:
#         for i, c in enumerate(numberList,1):
#             if findnumber == c:
#                 print("Found",findnumber,"at position",i)
#                 break
#             break
#         break
#     else:
#         print("Not found")