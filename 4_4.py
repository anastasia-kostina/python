from random import randint


my_list = [randint(1, 20) for i in range(15)]
new_list = [i for i in my_list if my_list.count(i) == 1]

print(f' Исходный список: {my_list}')
print(f' Итоговый список: {new_list}')
