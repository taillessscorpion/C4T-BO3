clist = ['red', 'blue', 'green']
print('Our color list.')
print(*clist, sep=', ')
while True:
    enter = input('Enter a new color to color list: ')
    if enter.isalpha():
        clist.append(enter)
        break
    else:
        print('Color {} does not exist.'.format(enter))
print('Our new color list.')
print(*clist, sep=', ')
