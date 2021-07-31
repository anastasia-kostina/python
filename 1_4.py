from sys import argv


def salary(hours, wage_rate, bonus):
    """ Возвращает заработную плату сотрудуника.

    hours -- выработка в часах (int)
    wage_rate -- ставка в час (float)
    bonus -- премия (float)
    результат wage -- размер заработной платы (float)
    """

    wage = int(hours) * float(wage_rate) + float(bonus)
    return wage


script_name, user_hours, user_wage_rate, user_bonus = argv
print(f'Заработная плата сотрудника составляет {salary(user_hours, user_wage_rate, user_bonus)}')
