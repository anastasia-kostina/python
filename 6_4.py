from itertools import count
from itertools import cycle
from random import randint

# итератор, генерирующий 10 целых чисел, начиная с указанного пользователем
n = input('Введите целое число: ')
try:
    n = int(n)
    for el in count(n):
        if el > n + 9:
            break
        else:
            print(el)
except ValueError:
    print('Введено не целое число!')

# итератор, повторяющий элементы списка, определенного заранее
my_list = [randint(1, 20) for i in range(10)]
print(f'Исходный список: {my_list}')
print(f'Итоговый список: ')
i = 0
for el in cycle(my_list):
    if i == len(my_list):
        break
    print(el)
    i += 1
