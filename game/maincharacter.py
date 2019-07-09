import json
maincharacter = {
    'pname': 'South Knight',
    'name': '---South Knight---',
    'level': 0,
    'experience': 0,
    'maxexperience': 50,
    'hp': 10,
    'strength': 1,
    'damage': 2,
    'armor': 1,
    'defense': 5,
    'hitrate': 10,
    'outfit': {},
    'weapon': {},
}
with open('maincharacter.json', 'w') as outfile:  
    json.dump(maincharacter, outfile)