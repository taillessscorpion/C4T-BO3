import json
weaponchess = [{
    'weaponchess1': 'Weapon Chess Lvl 1',
    'chess': [{
        'pname': 'Snake Sword',
        'name': 'weapon',
        'strength': 2,
        'damage': 5,
    }, {
        'pname': 'Snake Archery Bow',
        'name': 'weapon',
        'strength': 5,
        'damage': 2,
    }, {
        'pname': 'Snake Blade',
        'name': 'weapon',
        'strength': 5,
        'damage': 5,
    }],
}, {
    'weaponchess2': 'Weapon Chess Lvl 2',
    'chess': [{
        'pname': 'Bear Sword',
        'name': 'weapon',
        'strength': 4,
        'damage': 10,
    }, {
        'pname': 'Bear Archery Bow',
        'name': 'weapon',
        'strength': 10,
        'damage': 4,
    }, {
        'pname': 'Snake Blade',
        'name': 'weapon',
        'strength': 10,
        'damage': 10,
    }],
}, {
    'weaponchess3': 'Weapon Chess Lvl 3',
    'chess': [{
        'pname': 'Scorpion Sword',
        'name': 'weapon',
        'strength': 6,
        'damage': 15,
    }, {
        'pname': 'Scorpion Archery Bow',
        'name': 'weapon',
        'strength': 15,
        'damage': 6,
    }, {
        'pname': 'Scorpion Blade',
        'name': 'weapon',
        'strength': 15,
        'damage': 15,
    }],
}, {
    'weaponchess4': 'Weapon Chess Lvl 4',
    'chess': [{
        'pname': 'Tailless Sword',
        'name': 'weapon',
        'strength': 14,
        'damage': 20,
    }, {
        'pname': 'Snake Archery Bow',
        'name': 'weapon',
        'strength': 20,
        'damage': 14,
    }, {
        'pname': 'Snake Blade',
        'name': 'weapon',
        'strength': 20,
        'damage': 20,
    }],
}]
with open('weaponchess.json', 'w') as outfile:
    json.dump(weaponchess, outfile)