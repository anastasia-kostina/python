# родительский класс
class Car:
    # конструктор для инициализации значений атрибутов
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы класса
    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина повернула направо')
        if direction == 'left':
            print('Машина повернула налево')

    def show_speed(self):
        return self.speed


# дочерние классы
class TownCar(Car):

    def __init__(self, speed, color, name, is_police, passenger_seats, clirence):
        super().__init__(speed, color, name, is_police)
        self.passenger_seats = passenger_seats
        self.clirence = clirence

    def car_clirence(self):
        return self.clirence

    def passenger_number(self):
        return self.passenger_seats

    def show_speed(self):
        if self.speed < 60:
            print(f'Машина движется со скоростью {self.speed} км/ч')
        else:
            print('Машина превышает скорость')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police, max_velocity, has_turbo, has_spoiler):
        super().__init__(speed, color, name, is_police)
        self.max_velocity = max_velocity
        self.has_turbo = has_turbo
        self.has_spoiler = has_spoiler

    def maximum_velocity(self):
        print(f'Максимальная скорость спортивного авто: {self.max_velocity} км/ч')

    def turbo(self):
        if self.has_turbo:
            print('В машине есть турбированный двигатель')
        else:
            print('В машине нет турбированного двигателя')

    def spoiler(self):
        if self.has_spoiler:
            print('В машине есть спойлер')
        else:
            print('В машине нет спойлера')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police, car_type, mass):
        super().__init__(speed, color, name, is_police)
        self.car_type = car_type
        self.mass = mass

    def workcar_type(self):
        print(f'Это {self.car_type}')

    def mass_restriction(self):
        if self.mass > 50:
            return 'есть ограничение массы'
        else:
            return 'нет ограничения массы'

    def show_speed(self):
        if self.speed < 40:
            print(f'Машина движется со скоростью {self.speed} км/ч')
        else:
            print('Машина превышает скорость')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def priority_car(self):
        if self.is_police:
            print('Эта машина имеет приоритет при включении звуковой сирены и проблескового маячка')
        else:
            print('Эта машина не имеет приоритета')


# создаем экземпляры классов
print("Экземпляр класса Car")
c = Car(50, "white", "Lexus", False)
print(f"Это {c.color} {c.name}")
c.go()
c.turn('right')
c.turn('left')
c.stop()
print(f"Текущая скорость {c.name}: {c.show_speed()} км/ч")
print('')

print("Экземпляр класса TownCar")
tc = TownCar(80, "green", "Volga", False, 4, 17)
print(f"Это {tc.color} {tc.name}")
print(f'Эта машина может перевезти {tc.passenger_seats} пассажира')
print(f'Клиренс авто равен {tc.car_clirence()} см')
tc.show_speed()
print('')

print("Экземпляр класса SportCar")
sc = SportCar(100, "black", "Ferrari", False, 350, True, False)
print(f"Это {sc.color} {sc.name}")
sc.maximum_velocity()
sc.spoiler()
sc.turbo()
print('')

print("Экземпляр класса WorkCar")
wc = WorkCar(20, "yellow", "Kubota", False, 'трактор', 60)
print(f"Это {wc.color} {wc.name}")
wc.workcar_type()
print(f"На эту машину {wc.mass_restriction()}")
wc.show_speed()
print('')

print("Экземпляр класса PoliceCar")
pc = PoliceCar(60, "white", "Volkswagen", True)
print(f"Это {pc.color} {pc.name}")
pc.priority_car()
