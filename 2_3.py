def info(**kwargs):
    """ Возвращает данные о пользователе одной строкой.

    name -- имя (str)
    surname -- фамилия (str)
    date -- дата рождения (str)
    city -- город (str)
    email -- электронный адрес (str)
    phone -- телефон (str)
    """

    return print(f'имя: {kwargs["name"]}, фамилия: {kwargs["surname"]}, дата рождения: {kwargs["date"]}, '
                 f'город: {kwargs["city"]}, email: {kwargs["email"]}, телефон: {kwargs["phone"]}')


info(name=input('Введите имя: '), surname=input('Введите фамилию: '), date=input('Введите дату рождения: '),
     city=input('Введите город проживания: '), email=input('Введите email: '), phone=input('Введите телефон: '))
