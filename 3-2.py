try:
    # Запрашиваем номер месяца
    n = int(input('Введите порядковый номер месяца от 1 до 12: '))
except ValueError:
    # Проверяем являются ли введенные символы целым числом
    print('Ошибка! Попробуйте еще раз')
else:
    # Определяем время года через list
    if (n >= 1) and (n <= 12):
        times = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
        print(times[n - 1])
    else:
        print('Введенное число не принадлежит интервалу от 1 до 12!')

    # Решение через dict
    # Создаем словарь времен года
    dict_months = {
        'Зима': (12, 1, 2),
        'Весна': (3, 4, 5),
        'Лето': (6, 7, 8),
        'Осень': (9, 10, 11)
    }
    # Определяем месяц
    for key in dict_months.keys():
        if n in dict_months[key]:
            print(key)


