while True:
    strInput = input('Nhập một dãy số, cách nhau bởi dấu ", ": ')
    if strInput.isalpha() or strInput.isspace():
        print('Dãy số {} có chứa số không tồn tại. Mời nhập lại.'.format(strInput))
    else:
        print('Đã xác nhận dãy số {}'.format(strInput))
        break
numberList = list(strInput)
newList = []
newlist = []
lstrInput = len(numberList)
cospace = strInput.count(' ',0,lstrInput)
#Phần xóa space trong list
for i in range(cospace):
    lstrInput = len(numberList)
    lospace = strInput.find(' ',0,lstrInput)
    numberList.pop(lospace)
    strInput = ''.join(numberList)
cocomma = strInput.count(',',0,lstrInput)
#Có bao nhiêu dấu phẩy thì chạy bấy nhiêu lần
for j in range(0,cocomma):
    lstrInput = len(numberList)
    locomma = strInput.find(',',0,lstrInput)
    #Chuyển những phần đứng trước dấu phẩy trở thành phần tử của 1 list mới
    for t in range(0,locomma):
        newList.append(numberList[t])
    trans = ''.join(newList)
    intTrans = int(trans)
    newlist.append(intTrans)
    newList = []
    #Xóa những phần tử đứng trước dấu phẩy và dấu phẩy
    for l in range(0,locomma+1):
        numberList.pop(0)
        strInput = ''.join(numberList)
#Chuyển phần cuối cùng trở thành phần tử của list mới
trans = ''.join(numberList) 
intTrans = int(trans)
newlist.append(intTrans)
print(newlist)
#Tính độ dài của list
llist = len(newlist)
#Tạo sẵn list chứa các số chẵn
even = []
#Tìm số chẵn để cho vào list
for i in range(llist):
    a = int(newlist[i])
    b = a % 2
    if b == 0:
        even.append(str(a))
    else:
        pass
#Chuyển từ list thành string để in ra màn hình.
strEven = ''
lEven = len(even)
#Chạy vòng for thêm vào string từng phần tử của list
#Sau mỗi lần thêm phần tử, sẽ thêm dấu ', ' vào sau.
for j in range(lEven):
    strEven += ''.join(even[j])
    strEven += ', '
#Xóa dấu phẩy ở cuối string
lstrEven = len(strEven)
strEven = strEven[:lstrEven-1] + strEven[(lstrEven):]
strEven = strEven[:lstrEven-2] + strEven[(lstrEven-1):]
#In ra theo dang giống mẫu đề bài.
#Tất cả các số chắn trong danh sách là: 14, 53, 92, -4.
print('Tất cả các số chắn trong danh sách là: {}.'.format(strEven))
