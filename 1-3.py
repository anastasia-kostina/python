def division(a, b):
    """ Возвращает частное от деления.

    a -- делимое (float)
    b -- делитель (float)
    результат a/b -- частное (float)
    """
    try:
        return a/b
    except ZeroDivisionError:
        print("Деление на ноль!")
        return 'не определен'


n = float(input('Введите первое число: '))
m = float(input('Введите второе число: '))
print(f'Результат деления {n} на {m}: {division(n, m)}')

