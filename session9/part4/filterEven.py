numberList = ['14', '54', '92', '9', '-4', '-49']
#Chuyển list về string
strlist = ''.join(numberList)
#Tính độ dài của list
llist = len(numberList)
#Tạo sẵn list chứa các số chẵn
even = []
#Tìm số chẵn để cho vào list
for i in range(llist):
    a = int(numberList[i])
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
