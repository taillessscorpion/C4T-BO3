employee1 = {
    'Name': 'Huy',
    'Role': 'Waiter',
    'Hours': '12',
    'SalaryPerHour': '0.8',
}
employee2 = {
    'Name': 'Tung',
    'Role': 'Cook',
    'Hours': '24',
    'SalaryPerHour': '1.5',
}
employee3 = {
    'Name': 'M. Duc',
    'Role': 'Manager',
    'Hours': '20',
    'SalaryPerHour': '2',
}
listEmploy = [employee1, employee2, employee3]
for x in range(2):
    employeex = {
    'Name': '',
    'Role': '',
    'Hours': '',
    'SalaryPerHour': '',
}
    name = input('Nhập tên nhân viên: ')
    role = input('Nhập chức vụ nhân viên: ')
    hours = input('Nhập thời gian làm việc của nhân viên: ')
    salary = input('Nhập mức lương của nhân viên: ')
    employeex['Name'] = name
    employeex['Role'] = role
    employeex['Hours'] = hours
    employeex['SalaryPerHour'] = salary
    listEmploy.append(employeex)
for i, j in enumerate(listEmploy):
    print(j)