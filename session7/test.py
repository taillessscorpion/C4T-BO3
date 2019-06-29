middle = input('Mời nhập tên lót của bạn tại đây: ')
listmid = list(middle)
donemiddle = []
lenmid = len(middle)    
cospace = middle.count(' ', 0, lenmid) 
lospace = middle.find(' ', 0, lenmid)  
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
print(middle)
