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
for i in range(cospace):
    lstrInput = len(numberList)
    lospace = strInput.find(' ',0,lstrInput)
    numberList.pop(lospace)
    strInput = ''.join(numberList)
cocomma = strInput.count(',',0,lstrInput)
for j in range(0,cocomma): #chay 2 lan tu 0 toi 1 (co 2 dau phay)
    lstrInput = len(numberList) #do dai cua string input
    locomma = strInput.find(',',0,lstrInput) #tim vi tri cua dau phay
    for t in range(0,locomma):
        newList.append(numberList[t])
    trans = ''.join(newList)
    intTrans = int(trans)
    newlist.append(intTrans)
    newList = []
    for l in range(0,locomma+1):
        numberList.pop(0)
        strInput = ''.join(numberList)
trans = ''.join(numberList)
intTrans = int(trans)
newlist.append(intTrans)
print(newlist)






