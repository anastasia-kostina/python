class ComplexNumber:
    # выполняем перегрузку конструктора
    def __init__(self, zre, zim):
        self.zre = zre
        self.zim = zim

    # сложение 2 комплексных чисел
    def __add__(self, other):

        return ComplexNumber(self.zre+other.zre, self.zim+other.zim)

    # умножение 2 комплексных чисел
    def __mul__(self, other):

        return ComplexNumber(self.zre*other.zre-self.zim*other.zim, self.zim*other.zre+self.zre*other.zim)

    # вывод результата
    def __str__(self):
        if self.zim > 0:
            return f'{self.zre} + {self.zim}j'
        else:
            return f'{self.zre} - {abs(self.zim)}j'


# создаем экземпляры класса ComplexNumber:
a = ComplexNumber(-5, 1)
b = ComplexNumber(4, 1)
print(f'a+b = {a + b}')
print(f'a*b = {a * b}')

print(" ")
# проверка:
print((-5 + 1j) + (4 + 1j))
print((-5 + 1j) * (4 + 1j))
