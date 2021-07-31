from random import randint


my_list = [randint(1, 20) for i in range(15)]
new_list = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i] < my_list[i + 1]]

print(f' Исходный список: {my_list}')
print(f' Итоговый список: {new_list}')
