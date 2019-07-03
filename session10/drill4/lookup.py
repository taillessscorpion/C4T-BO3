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
    find = input('''Nhập tên một vị tướng trong Liên Minh (để dừng trương chình, gõ stop): ''')
    find = find.lower()
    listFindCharacters = list(find)
    listFindCharacters[0] = listFindCharacters[0].upper()
    find = ''.join(listFindCharacters)
    if find in champions:
        print('{} is {}'.format(find,champions[find]))
    elif find == 'Stop':
        print('Tạm biệt!')
        break
    else:
        print('''Vị tướng {} không tồn tại trong Liên Minh. Mời tìm vị tướng khác.'''.format(find))
