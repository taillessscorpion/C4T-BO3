distric = ['ST', 'BD', 'BTL', 'CG', 'ĐĐ', 'HBT']
acreage = ['11743', '9.224', '43.35', '12.04', '9.96', '10.09']
population = ['150300', '247100', '333300', '266800', '420900', '318000']
populationDensity = []
lenPopulation = len(population)
for x in range(lenPopulation):
    pdensity = int(population[x]) / float(acreage[x])
    populationDensity.append(pdensity)
Max = populationDensity[0]
Min = populationDensity[0]
for y in range(1,lenPopulation):
    if Max < populationDensity[y]:
        Max = populationDensity[y]
    elif Min > populationDensity[y]:
        Min = populationDensity[y]
for z in range(0,lenPopulation):
    if Max == populationDensity[z]:
        print('Quận {} có mật độ dân số cao nhất.'.format(distric[z]))
    elif Min == populationDensity[z]:
        print('Quận {} có mật độ dân số thấp nhất.'.format(distric[z]))

