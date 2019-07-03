inputList = input('Nhập vào một dãy số, phân biệt bởi " ": ')
sumlist = 0
numberList = list(inputList.split(' '))
for i, j in enumerate(numberList):
    sumlist += int(j)
print(sumlist)
