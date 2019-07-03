high = [15, 77, 200, 189, 34]
print('Điểm cao: ')
for i, j in enumerate(high,1):
    print('{}. {}'.format(i, j))
new = int(input('Nhập điểm cao mới: '))
high.append(new)
for i, j in enumerate(high,1):
    print('{}. {}'.format(i, j))
