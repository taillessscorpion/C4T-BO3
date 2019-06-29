from random import randint
w = randint(0,100)
if w < 31:
    print('Rainy')
elif w < 61:
    print('Cloudy')
else:
    print('Sunny')