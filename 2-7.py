from abc import ABC, abstractmethod


# создаем абстрактный класс
class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    # создаем абстрактный метод
    @abstractmethod
    def calculate(self):
        pass


# создаем класс-потомок абстракного класса
class Suit(Clothes):

    @property
    def calculate(self):
        return 2 * self.param + 0.3


# создаем класс-потомок абстракного класса
class Coat(Clothes):

    @property
    def calculate(self):
        return self.param / 6.5 + 0.5


V = 42
H = 1.5
# создаем экземпляры классов
s = Suit(H)
c = Coat(V)
print(f'Расход ткани для изгоовления костюма: {s.calculate}')
print(f'Расход ткани для изгоовления пальто: {c.calculate}')
print(f'Общий расход ткани: {c.calculate + s.calculate}')
