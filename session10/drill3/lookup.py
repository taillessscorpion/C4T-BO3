champions = {
    'Aatrox': '''the Darkin Blade''',
    'Ahri': '''the Nine-Tailed Fox''',
    'Akali': '''the Rogue Assassin''',
    'Alistar': '''the Minotaur''',
    'Amumu': '''the Sad Mummy''',
    'Anivia': '''the Cryophoenix''',
    'Annie': '''the Dark Child''',
}
while True:
    find = input('Nhập tên một vị tướng trong Liên Minh: ')
    if find in champions:
        print('{} is {}'.format(find,champions[find]))
        break
    else:
        print('Món {} không tồn tại. Mời tìm món khác.'.format(find))
