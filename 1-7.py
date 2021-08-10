import random


def arr_fill(n, m):
    """ Возвращает матрицу, заполненную произвольными числами от 0 до 19.

    n -- число строк (int)
    m -- число столбцов (int)

    результат arr -- матрица (int)
    """

    arr = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = random.randrange(0, 20)
    return arr


def len_rows(arr):
    """ Возвращает True, если все строки матрицы имеют одинаковую длину, и False в противном случае.

    arr -- список (int)

    результат True or False (bool)
    """
    row_len = []
    for i in range(0, len(arr)):
        row_len.append(len(arr[i]))
    if len(row_len) == row_len.count(row_len[0]):
        return True
    else:
        return False


class Matrix:
    # выполняем перегрузку конструктора
    def __init__(self, arr):
        self.arr = arr

    # вывод матрицы
    def __str__(self):
        out = []
        for row in self.arr:
            str1 = " "
            for el in row:
                str1 += " " + str(el).zfill(2)
            out.append(str1.lstrip())
        return '\n'.join(out)

    # сложение 2 матриц
    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.arr, other.arr):
            result1 = []
            for el1, el2 in zip(row1, row2):
                result1.append(el1 + el2)
            result.append(result1)
        return Matrix(result)


n = int(input("Введите число строк матрицы: "))
m = int(input("Введите число столбцов матрицы: "))

# создаем матрицы a и b
a = arr_fill(n, m)
b = arr_fill(n, m)
# проверка равенства длин строк матриц
if len_rows(a) and len_rows(b):
    # создаем экземпляры класса Matrix
    my_arr1 = Matrix(a)
    print("Вывод матрицы A")
    print(my_arr1)
    print(" ")
    print("Вывод матрицы B")
    my_arr2 = Matrix(b)
    print(my_arr2)
    print(" ")
    print("Вывод матрицы A+B")
    print(my_arr1 + my_arr2)
else:
    print('Строки матриц должны иметь одинаковую длину!')
