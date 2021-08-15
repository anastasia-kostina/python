class IsNumberErr(Exception):
    def __init__(self, text):
        self.txt = text


class IsNumber:
    # выполняем перегрузку конструктора
    def __init__(self, value):
        self.value = value

    @staticmethod
    def digit(value):
        if value.isdigit():
            return True
        else:
            try:
                float(value)
                return True
            except:
                raise IsNumberErr("Введенный символ не является числом")


my_str = ''
my_list = []
while True:
    try:
        if my_str == 'stop':
            break
        else:
            my_str = input('Введите элементы списка. Для прекращения ввода введите stop: ')
            if my_str != 'stop':
                if IsNumber.digit(my_str):
                    my_list.append(my_str)
    except IsNumberErr as err:
        print(err)
print(my_list)
