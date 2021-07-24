# Запрашиваем строку
str = input('Введите строку: ')
# Разделяем на слова
str = str.split()
# Выводим пронумерованные список слов
for i, el in enumerate(str):
    print(i+1, el[:10])
