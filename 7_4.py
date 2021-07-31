def my_factorial(number):
    """ Возвращает факториал числа.

    number -- число, факториал которого необходимо вычислить (int)
    number_fact -- результат (int)
    """
    number_fact = 1

    for i in range(2, number + 1):
        number_fact *= i
    return number_fact


def fact(n):
    """ Возвращает генератор чисел.

    n -- число элементов последовательности (int)
    результат -- последовательность целых чисел 1!,...n!
    """
    for i in range(1, n + 1):
        yield my_factorial(i)


n_fact = input('Введите целое число: ')
try:
    n_fact = int(n_fact)
    for el in fact(n_fact):
        print(el)
except ValueError:
    print('Введено не целое число!')
