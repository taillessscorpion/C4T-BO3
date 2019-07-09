import json
from random import randint
with open('maincharacter.json') as json_file:
    mc = json.load(json_file)
with open('monster.json') as json_file:
    ms = json.load(json_file)
with open('bonuschess.json') as json_file:
    bc = json.load(json_file)
def showindex(n):
    print('{}---{:02d}---{:03d}---{:03d}--{:03d}---{:03d}---{:03d}---{:03d}---{:.2f}'.format(mc['name'], mc['level'], mc['experience'], mc['hp'], mc['strength'], mc['damage'], mc['armor'], mc['defense'], mc['hitrate']/100))
    print('-----[ V S ]-------[LVL]-[EXP]-[HP]-[STR]-[DMG]-[AMR]-[DEF]-[HRT]')
    print('{}---{:02d}---{:03d}---{:03d}--{:03d}---{:03d}---{:03d}---{:03d}---{:.2f}'.format(ms[n]['name'], ms[n]['level'], ms[n]['experience'], ms[n]['hp'], ms[n]['strength'], ms[n]['damage'], ms[n]['armor'], ms[n]['defense'], ms[n]['hitrate']/100))
def combat(a,d):
    rhr = randint(0,d['hitrate']+d['defense'])
    if a['hitrate'] >= rhr:
        antiarmor = a['strength'] - d['armor']
        if antiarmor > 0:
            d['hp'] -= a['damage'] + antiarmor
            print('{} received {} damage from {}'.format(d['pname'], a['damage'] + antiarmor, a['pname']))
        else:
            d['hp'] -= a['damage']
            print('{} received {} damage from {}'.format(d['pname'], a['damage'], a['pname']))
    else:
        print('{} dodge a hit from {}.'.format(d['pname'], a['pname']))
    return d['hp']
def exp(k,d):
    reallevel = d['level'] - k['level']
    if reallevel > 0:
        expreceive = 5 * reallevel
    elif -4 <= reallevel <= 0:
        expreceive = 5 + reallevel
    else:
        expreceive = 0
    return expreceive
def respawn():
    ms[Choose]['hp'] = mfullhp
    ms[Choose]['killed'] += 1
    return ms[Choose]['killed']
def rewardB(a):
    lucky = randint(0,5)
    namelucky = bc[a]['chess'][lucky]['name']
    valuelucky = bc[a]['chess'][lucky]['value']
    print('{} received {} {} from Reward: {}.'.format(mc['pname'], valuelucky, namelucky, bc[a]['chess'][lucky]['pname']))
    return (namelucky, valuelucky)
while True:
    print('.. {} Level: {:02d}, HP: {:03d}, EXP: {:03d}/{:03d}, STR: {:03d}, DMG: {:03d}, AMR: {:03d}, DEF: {:03d}, HRT: {:.2f}'.format(mc['name'], mc['level'], mc['hp'], mc['experience'], mc['maxexperience'], mc['strength'], mc['damage'], mc['armor'], mc['defense'], mc['hitrate']/100))
    for i, j in enumerate(ms,1):
        print('{}. {} Level: {:02d}, HP: {:03d}, Dead: {:06d}, STR: {:03d}, DMG: {:03d}, AMR: {:03d}, DEF: {:03d}, HRT: {:.2f}'.format(i, j['name'], j['level'], j['hp'], j['killed'], j['strength'], j['damage'], j['armor'], j['defense'], j['hitrate']/100 ))
    choose = input('Choose monster to fight.    ')
    Choose = int(choose) - 1
    showindex(Choose)
    fullhp = mc['hp']
    mfullhp = ms[Choose]['hp']
    while True:
        if mc['hp'] > 0:
            ms[Choose]['hp'] = combat(mc,ms[Choose])
        elif mc['hp'] <= 0:
            print("{} is dead!! {} has just killed {}".format(mc['pname'], ms[Choose]['pname'], mc['pname']))
            break
        if ms[Choose]['hp'] > 0:
            mc['hp'] = combat(ms[Choose], mc)
        elif ms[Choose]['hp'] <= 0:
            mc['experience'] += exp(mc, ms[Choose])
            mc['hp'] = fullhp
            print("{} is dead!! {} has just killed {}".format(ms[Choose]['pname'], mc['pname'], ms[Choose]['pname']))
            print('{} received {} experience point(s).'.format(mc['pname'], exp(mc, ms[Choose])))
            a, b = rewardB(ms[Choose]['given'])
            mc[a] += b
            ms[Choose]['killed'] = respawn()
            break
        if mc['hp'] <= 0:
            print("{} is dead!! {} has just killed {}".format(mc['pname'], ms[Choose]['pname'], mc['pname']))
            break
    if mc['experience'] >= mc['maxexperience']:
        newexp = mc['experience'] - mc['maxexperience']
        mc['level'] += 1
        mc['experience'] = newexp
        mc['maxexperience'] *= 2
        mc['hp'] += 10
        mc['strength'] += 2
        mc['damage'] += 2
        mc['armor'] += 2
        mc['defense'] += 5
        mc['hitrate'] += 5
        print('LEVEL UP. Now, {} are level {}'.format(mc['pname'], mc['level']))
    if ms[6]['killed'] >= 1:
        print('{} has killed Boss {}.'.format(mc['pname'], ms[6]['pname']))
        print('GAME OVER')
        break
    if mc['hp'] <= 0:
        print('GAME OVER')
        break