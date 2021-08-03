out_myf = open("my_file.txt", "w")
my_lines = []
# заполнение списка my_lines строками пользователя
line = True
while line:
    line = input("Введите строки для записи. Для прекращения записи введите пустую строку. ")
    if line:
        my_lines.append(line + '\n')
# запись строк в файл
out_myf.writelines(my_lines)
out_myf.close()
