class Worker:
    # конструктор для инициализации значений атрибутов
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    # методы класса
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# создаем первый экземпляр класса
my_worker1 = Position('Liu', 'Li', 'Seller', 20000, 10000)
print(f'Имя первого работника {my_worker1.get_full_name()}')
print(f'Должность первого работника {my_worker1.position}')
print(f'Доход первого работника {my_worker1.get_total_income()}')
print('')

# создаем второй экземпляр класса
worker2_name = input("Введите имя работника: ")
worker2_surname = input("Введите фамилию работника: ")
worker2_position = input("Введите должность работника: ")
worker2_wage = input("Введите зарплату работника: ")
worker2_bonus = input("Введите премию работника: ")
print('')

# проверяем коррекность введеного имени, фамилии и должности
if not worker2_name.isalpha():
    print('Недопустимое имя!')
elif not worker2_surname.isalpha():
    print('Недопустимая фамилия!')
elif not worker2_position.isalpha():
    print('Недопустимая должность!')
else:
    # проверяем коррекность введеного дохода для заполнения словаря
    try:
        worker2_wage = float(worker2_wage)
        worker2_bonus = float(worker2_bonus)
        my_worker2 = Position(worker2_name, worker2_surname, worker2_position, worker2_wage, worker2_bonus)
        print(f'Имя второго работника {my_worker2.get_full_name()}')
        print(f'Должность второго работника {my_worker2.position}')
        print(f'Доход второго работника {my_worker2.get_total_income()}')
    except ValueError:
        print('Некорректно введены доходы сотрудника!')
