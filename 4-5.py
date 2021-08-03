with open("my_file4.txt", "r") as f1, open("my_file4-2.txt", "w+", encoding="utf-8") as f2:
    for line in f1:
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        f2.write(line)
