# родительский класс
class Stationery:

    # конструктор для инициализации значений атрибута
    def __init__(self, title):
        self.title = title

    # метод класса
    def draw(self):
        print('Запуск отрисовки')


# дочерние классы
class Pen(Stationery):

    def __init__(self, title='Pen'):
        super().__init__(title)

    def draw(self):
        print(f'Рисование with {self.title}')


class Pencil(Stationery):

    def __init__(self, title='Pencil'):
        super().__init__(title)

    def draw(self):
        print(f'Рисование with {self.title}')


class Handle(Stationery):

    def __init__(self, title='Handle'):
        super().__init__(title)

    def draw(self):
        print(f'Рисование with {self.title}')


# создаем экземпляры классов
my_stationery = Stationery('Stationery')
my_stationery.draw()
my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
