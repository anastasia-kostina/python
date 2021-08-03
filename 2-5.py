count_lines = 0
with open("my_file2.txt") as out_myf2:
    for line in out_myf2:  # подсчет количества строк и слов в каждой строке
        count_lines += 1
        count_words = 1
        for el in line:
            if el == ' ':
                count_words += 1
        print(f'{count_lines}я строка: {line} (количество слов: {count_words})')

print(f'Количество строк в файле: {count_lines}')
