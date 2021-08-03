from random import randint

# запись 5 чисел, разделенных пробелами, в файл
with open("my_file5.txt", "w") as f:
    for i in range(5):
        f.write(str(randint(1, 10)))
        if i != 5:
            f.write(" ")

# подсчет суммы чисел
i = 0
with open("my_file5.txt", "r") as f:
    my_list = f.read()
    my_list = my_list.split()
    for el in my_list:
        i += int(el)
print(f'Последовательность: {my_list}')
print(f'Сумма чисел последовательности: {i}')
