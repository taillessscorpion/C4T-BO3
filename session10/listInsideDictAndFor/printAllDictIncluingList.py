Lol = {
    'Name': 'LOL',
    'Year': 2010,
    'Characters': ['a', 'b', 'c', 'd'],
    'Nation': 'USA',
}
for k, v in Lol.items():
    if v == Lol['Characters']:
        for i, j in enumerate(v):
            print('{}: {}'.format(k, j))
    elif v != Lol['Characters']:
        print('{}: {}'.format(k, v))