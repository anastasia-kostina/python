class Road:
    # конструктор для инициализации значений атрибутов
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # метод класса
    def mass(self, m1cm, thickness):
        m = self._length * self._width * m1cm * thickness
        return m


# запрашиваем параметры
user_m = input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: ')
user_length = input('Введите длину дороги в м: ')
user_width = input('Введите ширину дороги в м: ')
user_thickness = input('Введите число см толщины полотна: ')

# создаем экземпляр класса
try:
    user_dens = float(user_m)
    user_length = float(user_length)
    user_width = float(user_width)
    user_thickness = float(user_thickness)
    r = Road(user_length, user_width)
    print(r.mass(user_dens, user_thickness))
except ValueError:
    print('Некорректно введенные данные!')
