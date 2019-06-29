print('XIN CHÀO BẠN ĐẾN VỚI GAME ĐẢO CHỮ.')
point = 0
while True:
    list_game=['family', 'grandma', 'father', 'mother', 'brother', 'sister', 'house', 'uncle', 'aunt', 'daddy', 'mamy']
    from random import randint
    import random
    llist = len(list_game)
    rd = randint(0,llist-1)
    game = list_game[rd]
    game0 = list(game)
    game1 = list(game)
    random.shuffle(game1)
    print('Từ cần sắp xếp lại là: ', *game1, sep='')
    play = input('Đáp án của bạn là: ')
    play1 = list(play)
    if play1 == game0:
        point += 1
        print('Chúc mừng. {} là một đáp án đúng. Bạn đạt được {} điểm.'.format(play, point))
    if play1 != game0:
        play1[0] = play1[0].upper()
        plp = ''.join(play1)
        print('{} là một đáp án không chính xác. Điểm của bạn là {}.'.format(plp, point))
        print('TẠM BIỆT.')
        break