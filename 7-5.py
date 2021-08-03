import json

profit = 0
avg_profit = 0
i = 1
my_list=[]
dict_firms={}
dict_profit={}
# построчное чтение файла
with open("my_file7.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, organization, income, losses = line.split() # распаковка строк в переменные
        profit = int(income) - int(losses) # расчет прибыли
        print(f'Прибыль {i}я фирма: {profit}')
        if profit > 0: # учет положительного дохода
            avg_profit += profit
        i += 1
        key, value = name, profit # создаем словарь с фирмами и их прибылью
        dict_firms[key] = value
    avg_profit = avg_profit / (i - 1) # расчет средней прибыли
    print(f'Средняя прибыль: {avg_profit}')
    dict_profit = {"average_profit": avg_profit} # создаем словарь средней прибыли
    my_list = [dict_firms, dict_profit] # создаем cписок
print(f'Итоговый список: {my_list}')

# сериализация списка
with open("my_file7-2.json", "w") as write_f:
    json.dump(my_list, write_f)