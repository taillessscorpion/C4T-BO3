import json
from random import randint
with open('bonuschess.json') as json_file:
    bc = json.load(json_file)
with open('maincharacter.json') as json_file:
    mc = json.load(json_file)
def rewardB(a):
    lucky = randint(0,5)
    namelucky = bc[a]['chess'][lucky]['name']
    valuelucky = bc[a]['chess'][lucky]['value']
    print('{} received {} {} from {}.'.format(mc['pname'], valuelucky, namelucky, bc[a]['chess'][lucky]['pname']))
    return (namelucky, valuelucky)
a, b = rewardB(0)
print(a)
print('{}---{:02d}---{:03d}---{:03d}--{:03d}---{:03d}---{:03d}---{:03d}---{:.2f}'.format(mc['name'], mc['level'], mc['experience'], mc['hp'], mc['strength'], mc['damage'], mc['armor'], mc['defense'], mc['hitrate']/100))