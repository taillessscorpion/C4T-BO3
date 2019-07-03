listOfDict = [{
    'Name': 'LOL',
    'Year': 2010,
    'Characters': ['a', 'b', 'c', 'd'],
},
{
    'Name': 'FIFA',
    'Year': 2007,
    'Characters': ['1', '2', '3', '4', '5'],
}]
for i, j in enumerate(listOfDict):
    nameNation = input('Nhập tên quốc gia: ')
    d = listOfDict[i]
    d['Nation'] = nameNation
print(listOfDict)