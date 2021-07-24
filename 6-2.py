# Задаем общее число товаров
numbers = int(input('Введите общее количество товаров: '))
# Задаем переменную-счетчик
count = 0
# Задаем список товаров
item_list = []
# Заполняем список товаров
while count < numbers:
    count += 1  # Обновляем переменную-счетчик
    print(f'{count}й товар')
    dict_item = {}  # Создаем словарь
    tuple_item = (count,)  # Создаем кортеж
    dict_item = {  # Заполняем словарь
        'Название': input('Введите название товара: '),
        'Цена': float(input('Введите цену товара: ')),
        'Количество': int(input('Введите количество товара: ')),
        'Ед.': input('Введите единицу измерения: ')
    }
    tuple_item = tuple_item + (dict_item,)  # Заполняем кортеж
    item_list.append(tuple_item)  # Добавляем элемент в список
# Выводим полученный список
for el in item_list:
    print(el)

dict_analytics = {}
for el in item_list:  # Осуществляем перебор по элементам списка
    for keys, vals in el[1].items():  # Осуществляем перебор по словарю
        dict_analytics[keys] = dict_analytics.get(keys, [])
        if vals not in dict_analytics.get(keys, []):
            dict_analytics.get(keys, []).append(vals)  # Заполняем словарь значениями

print(dict_analytics)
