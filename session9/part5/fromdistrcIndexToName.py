distric = ['ST', 'BD', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = ['150300', '247100', '333300', '266800', '420900', '318000']
lenPopulation = len(population)
Max = int(population[0])
Min = int(population[0])
for i in range(1,lenPopulation):
    if Max < int(population[i]):
        Max = int(population[i])
    elif Min > int(population[i]):
        Min = int(population[i])
for i in range(0,lenPopulation):
    if Max == int(population[i]):
        print('Quận có số dân đông nhất là {}.'.format(distric[i]))
    elif Min == int(population[i]):
        print('Quận có số dân ít nhất là {}.'.format(distric[i]))
