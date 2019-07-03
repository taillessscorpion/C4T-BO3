Lol = {
    'Name': 'LOL',
    'Year': 2010,
    'Characters': ['a', 'b', 'c', 'd'],
    'Nation': 'USA',
}
Lol['Characters'] = [1, 2, 3, 4]
for k, v in Lol.items():
    print('{} - {}.'.format(k, v))