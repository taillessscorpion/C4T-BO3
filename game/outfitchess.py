import json
outfitchess = [{
    'outfitchess1': 'Outfit Chess Lvl 1',
    'chess': [{
        'pname': 'Head Armour Lvl 1',
        'name': 'head',
        'armor': 1,
        'damage': 2,
    }, {
        'pname': 'Hands Armour Lvl 1',
        'name': 'hand',
        'armor': 1,
        'strength': 2,
    }, {
        'pname': 'Legs Armour Lvl 1',
        'name': 'leg',
        'armor': 1,
        'hitrate': 5,
    }, {
        'pname': 'Chest Armour Lvl 1',
        'name': 'chest',
        'armor': 1,
        'defense': 5,
    }, {
        'pname': 'Back Armour Lvl 1',
        'name': 'back',
        'armor': 1,
        'hp': 10,
    }],
}, {
    'outfitchess2': 'Outfit Chess Lvl 2',
    'chess': [{
        'pname': 'Head Armour Lvl 2',
        'name': 'head',
        'armor': 2,
        'damage': 4,
    }, {
        'pname': 'Hands Armour Lvl 2',
        'name': 'hand',
        'armor': 2,
        'strength': 4,
    }, {
        'pname': 'Legs Armour Lvl 2',
        'name': 'leg',
        'armor': 2,
        'hitrate': 10,
    }, {
        'pname': 'Chest Armour Lvl 2',
        'name': 'chest',
        'armor': 2,
        'defense': 10,
    }, {
        'pname': 'Back Armour Lvl 2',
        'name': 'back',
        'armor': 2,
        'hp': 20,
    }],
}, {
    'outfitchess3': 'Outfit Chess Lvl 3',
    'chess': [{
        'pname': 'Head Armour Lvl 3',
        'name': 'head',
        'armor': 3,
        'damage': 6,
    }, {
        'pname': 'Hands Armour Lvl 3',
        'name': 'hand',
        'armor': 3,
        'strength': 6,
    }, {
        'pname': 'Legs Armour Lvl 3',
        'name': 'leg',
        'armor': 3,
        'hitrate': 15,
    }, {
        'pname': 'Chest Armour Lvl 3',
        'name': 'chest',
        'armor': 3,
        'defense': 15,
    }, {
        'pname': 'Back Armour Lvl 3',
        'name': 'back',
        'armor': 3,
        'hp': 30,
    }],
}, {
    'outfitchess4': 'Outfit Chess Lvl 4',
    'chess': [{
        'pname': 'Head Armour Lvl 4',
        'name': 'head',
        'armor': 4,
        'damage': 8,
    }, {
        'pname': 'Hands Armour Lvl 4',
        'name': 'hand',
        'armor': 4,
        'strength': 8,
    }, {
        'pname': 'Legs Armour Lvl 4',
        'name': 'leg',
        'armor': 4,
        'hitrate': 20,
    }, {
        'pname': 'Chest Armour Lvl 4',
        'name': 'chest',
        'armor': 4,
        'defense': 20,
    }, {
        'pname': 'Back Armour Lvl 4',
        'name': 'back',
        'armor': 4,
        'hp': 40,
    }],
}]
with open('oufitchess.json', 'w') as outfile:
    json.dump(outfitchess, outfile)