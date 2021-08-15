class Date:

    # выполняем перегрузку конструктора
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def extract(cls, str_date):
        try:
            arr_date = str_date.split('-')
            day = int(arr_date[0])
            month = int(arr_date[1])
            year = int(arr_date[2])
            return day, month, year
        except Exception:
            print("Ошибка извлечения даты!")

    @staticmethod
    def validate(str_date):
        arr_date = str_date.split('-')
        day = int(arr_date[0])
        month = int(arr_date[1])
        year = int(arr_date[2])
        if day not in range(1, 32):
            print("Некорректное число!")
        elif month not in range(1, 13):
            print("Некорректный месяц!")
        elif year not in range(0, 2023):
            print("Некорректный год!")


my_date1 = "01/12/2012"
print(Date.extract(my_date1))
print(" ")
my_date2 = "00-12-2012"
print(Date.extract(my_date2))
Date.validate(my_date2)
print(" ")
my_date3 = "01-12-2012"
print(Date.extract(my_date3))
Date.validate(my_date3)
