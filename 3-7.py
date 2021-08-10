class Cell:
    # выполняем перегрузку конструктора
    def __init__(self, num):
        self.num = num

    # сложение 2 клеток
    def __add__(self, other):
        return Cell(self.num + other.num)

    # вычитание 2 клеток
    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            return 'Операция не может быть выполнена. Разность количества ячеек двух клеток должна быть больше нуля.'

    # умножение 2 клеток
    def __mul__(self, other):
        return Cell(self.num * other.num)

    # деление 2 клеток
    def __truediv__(self, other):
        if self.num // other.num > 0:
            return Cell(self.num // other.num)
        else:
            return 'Операция не может быть выполнена. Количество ячеек результирующей клетки должно быть больше нуля.'

    # вывод результата
    def __str__(self):
        return self.num * "*"

    # метод make_order
    def make_order(self, param):
        str = ''
        for i in range(0, self.num):
            str = str + '*'
            if i % param == param - 1:
                str = str + '\n'
        print(str)


# создаем экземпляры класса Cell:
n_c1 = input("Введите количество ячеек первой клетки: ")
n_c2 = input("Введите количество ячеек второй клетки: ")
m = input("Введите количество ячеек в ряду: ")

try:
    n_c1 = int(n_c1)
    n_c2 = int(n_c2)
    m = int(m)
    c1 = Cell(n_c1)
    c2 = Cell(n_c2)
    print(f'Первая клетка: {c1}')
    print(f'Вторая клетка: {c2}')
    print(f"Результат сложения клеток: {c1 + c2}")
    print(f"Результат вычитания клеток: {c1 - c2}")
    print(f"Результат вычитания клеток: {c2 - c1}")
    print(f"Результат умножения клеток: {c1 * c2}")
    print(f"Результат деления клеток: {c1 / c2}")
    c1.make_order(m)
    print(' ')
    c2.make_order(m)
except ValueError:
    print('Некорректно введенные данные!')
