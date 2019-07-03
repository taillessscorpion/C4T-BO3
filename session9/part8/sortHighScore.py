high = [15, 77, 34, 99, 14, 101, 109]
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
    high5.append(str(B))
    lenhigh5 = len(''.join(high5))
    high.remove(B)
    i += 1
for c, d in enumerate(high5,1):
    print('{}. {}'.format(c, d))



