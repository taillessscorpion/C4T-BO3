charater = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf', 'FlintStone'],
    'Pocket': ['MonsterDex', 'Flashlight'],
    'Gold': 150,
    'Level': 2,
}
charater['Skill'] = [{
    'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3,
}, {
    'Name': 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,
}, {
    'Name': 'Strong kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2,
}]
from random import *
rhitrate = uniform(0,1)
print('Bạn có thể chọn những trò sau để phang nó: ')
for i, j in enumerate(charater['Skill'],1):
    print(i, j['Name'])
skillchoice = int(input('Chọn chiêu để chơi nó: ')) - 1
if charater['Skill'][skillchoice]['Minimum level'] <= charater['Level']:
    if charater['Skill'][skillchoice]['Hit rate'] > rhitrate:
        print('Bạn đã gây ra {} damage lên thằng ngáo đó'.format(charater['Skill'][skillchoice]['Damage']))
    else:
        print('Đm, bạn đã ra đòn xịt')
else:
    print('Bạn cần tăng lên {} nữa mới có thể sử dụng chiêu'.format(charater['Skill'][skillchoice]['Minimum level']-charater['Level']))