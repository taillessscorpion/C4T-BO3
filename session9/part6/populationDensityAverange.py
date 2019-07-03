distric = ['ST', 'BD', 'BTL', 'CG', 'ĐĐ', 'HBT']
acreage = ['11743', '9.224', '43.35', '12.04', '9.96', '10.09']
population = ['150300', '247100', '333300', '266800', '420900', '318000']
lenPopulation = len(population)
pdensity = 0
for x in range(lenPopulation):
    pdensity += int(population[x]) / float(acreage[x])
averange = pdensity/int(lenPopulation)
print('Mật độ dân số trung bình của các quận là {0:.2f} người/km2.'.format(round(averange,2)))
