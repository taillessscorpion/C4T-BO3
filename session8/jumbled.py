import random
word = input('Nhập một từ bất kì: ')
list1 = list(word)
print(list1)
random.shuffle(list1)
for i in list1:
    print(i)
