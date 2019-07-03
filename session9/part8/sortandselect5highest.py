high = [15, 77, 34, 99, 14, 101]
high5 = []
print('Điểm cao: ')
i = 0
while i < 5:
    B = 0
    for a, b in enumerate(high):
        if B < b:
            B = b
        else:
            pass
    high5.append(int(B))
    high.remove(B)
    i += 1

for c, d in enumerate(high5,1):
    print('{}. {}'.format(c, d))

new = int(input('Nhập điểm cao mới: '))
high5.append(new)
i = 0
high5n = []
while i < 5:
    B = 0
    for a, b in enumerate(high5):
        if B < int(b):
            B = int(b)
        else:
            pass
    high5n.append(str(B))
    high5.remove(int(B))
    i += 1

for c, d in enumerate(high5n,1):
    print('{}. {}'.format(c, d))


