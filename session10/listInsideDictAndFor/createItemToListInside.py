Lol = {
    'Name': 'LOL',
    'Year': 2010,
    'Characters': ['a', 'b', 'c', 'd'],
    'Nation': 'USA',
}
Lol['Characters'].append('e')
for k, v in Lol.items():
    print('{} - {}.'.format(k, v))