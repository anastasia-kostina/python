dict_lesson = {}
# построчное чтение файла
with open("my_file6.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.split()  # разделяем на строки
        sum = 0
        for el in line:  # считаем сумму чисел в каждой строке
            s = "".join(i for i in el if i in "0123456789")
            if len(s) > 0:
                sum += int(s)
        key = line[0].strip(":")  # формируем словарь
        dict_lesson[key] = sum
print(dict_lesson)
