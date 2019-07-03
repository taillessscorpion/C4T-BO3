listEmploy = [{
    'Name': 'Huy',
    'Role': 'Waiter',
    'Hours': 12,
    'SalaryPerHour': 0.8,
}, {
    'Name': 'Tung',
    'Role': 'Cook',
    'Hours': 24,
    'SalaryPerHour': 1.5,
}, {
    'Name': 'M. Duc',
    'Role': 'Manager',
    'Hours': 20,
    'SalaryPerHour': 2,
}]
total = 0
for i in range(3):
    dictEmploy = listEmploy[i]
    wage = dictEmploy['Hours'] * dictEmploy['SalaryPerHour']
    total += wage
print('Lương của tất cả nhân viên là {:.2f} đô.'.format(round(total,2)))