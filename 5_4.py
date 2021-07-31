from functools import reduce


def multiplication(prev_el, el):
    """ Возвращает произведение элементов списка.

    prev_el -- предыдущий элемент (int)
    el -- текущий элемент (int)
    результат -- произведение элементов (int)
    """
    return prev_el * el


my_list = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(multiplication, my_list))
