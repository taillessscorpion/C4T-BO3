import json
bonuschess = [{
    'bonuschess1': 'Bonus Chess Lvl 1',
    'chess': [{
        'pname': 'HP Increase Lvl 1',
        'name': 'hp',
        'value': 5,
    }, {
        'pname': 'Strength Increase Lvl 1',
        'name': 'strength',
        'value': 1,
    }, {
        'pname': 'Damage Increase Lvl 1',
        'name': 'damage',
        'value': 1,
    }, {
        'pname': 'Armor Increase Lvl 1',
        'name': 'armor',
        'value': 1,
    }, {
        'pname': 'Defense Increase Lvl 1',
        'name': 'defense',
        'value': 5,
    }, {
        'pname': 'Hitrate Increase Lvl 1',
        'name': 'hitrate',
        'value': 5,
    }],
}, {
    'bonuschess2': 'Bonus Chess Lvl 2',
    'chess': [{
        'pname': 'HP Increase Lvl 2',
        'name': 'hp',
        'value': 10,
    }, {
        'pname': 'Strength Increase Lvl 2',
        'name': 'strength',
        'value': 2,
    }, {
        'pname': 'Damage Increase Lvl 2',
        'name': 'damage',
        'value': 2,
    }, {
        'pname': 'Armor Increase Lvl 2',
        'name': 'armor',
        'value': 2,
    }, {
        'pname': 'Defense Increase Lvl 2',
        'name': 'defense',
        'value': 10,
    }, {
        'pname': 'Hitrate Increase Lvl 2',
        'name': 'hitrate',
        'value': 10,
    }],
}, {
    'bonuschess3': 'Bonus Chess Lvl 3',
    'chess': [{
        'pname': 'HP Increase Lvl 3',
        'name': 'hp',
        'value': 15,
    }, {
        'pname': 'Strength Increase Lvl 3',
        'name': 'strength',
        'value': 3,
    }, {
        'pname': 'Damage Increase Lvl 3',
        'name': 'damage',
        'value': 3,
    }, {
        'pname': 'Armor Increase Lvl 3',
        'name': 'armor',
        'value': 3,
    }, {
        'pname': 'Defense Increase Lvl 3',
        'name': 'defense',
        'value': 15,
    }, {
        'pname': 'Hitrate Increase Lvl 3',
        'name': 'hitrate',
        'value': 15,
    }],
}, {
    'bonuschess4': 'Bonus Chess Lvl 4',
    'chess': [{
        'pname': 'HP Increase Lvl 4',
        'name': 'hp',
        'value': 20,
    }, {
        'pname': 'Strength Increase Lvl 4',
        'name': 'strength',
        'value': 4,
    }, {
        'pname': 'Damage Increase Lvl 4',
        'name': 'damage',
        'value': 4,
    }, {
        'pname': 'Armor Increase Lvl 4',
        'name': 'armor',
        'value': 4,
    }, {
        'pname': 'Defense Increase Lvl 4',
        'name': 'defense',
        'value': 20,
    }, {
        'pname': 'Hitrate Increase Lvl 4',
        'name': 'hitrate',
        'value': 20,
    }],
}]
with open('bonuschess.json', 'w') as outfile:
    json.dump(bonuschess, outfile)