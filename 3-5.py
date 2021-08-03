# чтение файла
with open("people.txt", "r") as wage:
    content = wage.read()
    print(content)

content = content.split()
# преобразуем в словарь
dict_content = {content[i]: int(content[i + 1]) for i in range(0, len(content), 2)}
print('Сотрудники, чей оклад менее 20000: ')
av_wage = 0
for key, value in dict_content.items():
    av_wage += value
    if value < 20000:
        print(key)
av_wage = av_wage / len(dict_content)
print(f'Средний доход сотрудника равен {av_wage}')
