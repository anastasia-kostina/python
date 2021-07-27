def my_func(a, b, c):
    """ Возвращает сумму двух наибольших чисел.

    a -- первое число (float)
    b -- второе число (float)
    с -- третье число (float)
    результат summa -- сумма (float)
    """
    summa = a + b
    if summa < (a + c):
        summa = a + c
    if summa < (b + c):
        summa = b + c
    return summa


num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))
print(f'Cумма двух максимальных чисел равна {my_func(num1, num2, num3)}')
