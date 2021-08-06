import time


class TrafficLight:
    colors = ['red', 'yellow', 'green']

    times = {'red': 7, 'yellow': 2, 'green': 3}

    c_prints = {'red': '31m', 'yellow': '33m', 'green': '32m'}

    # конструктор для инициализации значений атрибутов
    def __init__(self, color):
        self.__color = color

    # метод класса
    def running(self):

        color_index = self.colors.index(self.__color)
        i = color_index
        while True:
            for el in self.colors[i:] + self.colors[:]:
                print(f'Горит \033[0;{self.c_prints[el]}{el}\033[0m')
                time.sleep(self.times[el])
                i += 1
                if i > 5:
                    break
            break
        print('Светофор завершил работу')


# создаем экземпляр класса
t = TrafficLight('yellow')
t.running()
