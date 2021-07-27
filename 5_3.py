def sum_numbers():
    """ Сумма чисел, введенная пользователем.

    результат -- summa (int)
    """
    my_list = []
    ok = True

    while ok:
        my_str = (input('Введите целые числа, разделенные пробелом. Для прекращения ввода введите символ *: '))
        my_str = my_str.split()
        for i in my_str:
            if i == '*':
                ok = False
                break
            else:
                try:
                    my_list.append(int(i))
                except ValueError:
                    continue
        summa = sum(my_list)
        print(summa)
    return f'Общая сумма введенных чисел составила: {summa}'


print(sum_numbers())
