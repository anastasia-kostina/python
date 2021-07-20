# Числа
a = 5  # int
b = 5.5  # float
print(a)
print(b)
# Строки
my_string = 'Hello'
print(my_string)
# Списки
my_list = [1, 'c', 1.2]
print(my_list)
# Словари
my_dictionary = {'item': 'Chair', 'quantity': 5, 'color': 'black'}
print(my_dictionary)
# Кортежи
my_tuple = ('d', 3, 3.2)
print(my_tuple)
# Множества
my_set = {2.2, 'Nastya', 2}
print(my_set)

name = input("Введите Ваше полное имя: ")
print(f'Привет, {name}!')  # через f-строку
print("Привет, %s!" % name)  # через оператор %
surname = input("Введите Вашу фамилию: ")
middle_name = input("Введите Ваше отчество: ")
print(f'Ваше полное имя: {surname} {name} {middle_name}')  # через f-строку
print('Ваше полное имя: %s %s %s' % (surname, name, middle_name))  # через оператор %
num1 = int(input("Введите произвольное целое число: "))
print(f'Вы ввели целое число {num1}')  # через f-строку
print("Вы ввели целое число %d" % num1)  # через оператор %
num2 = float(input("Введите произвольное дробное число: "))
print(f'Вы ввели дробное число {num2}')  # через f-строку
print("Вы ввели дробное число %f" % num2)  # через оператор %
