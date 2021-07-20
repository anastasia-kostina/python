n = int(input("Введите число n: "))
# Перерводим число n в строку
n_temp = str(n)
# Составляем строку nn
nn_temp = n_temp + n_temp
# Составляем строку nnn
nnn_temp = n_temp + n_temp + n_temp
# Вычисляем сумму чисел n+nn+nnn
n_sum = n + int(nn_temp) + int(nnn_temp)
print(f'Сумма чисел n+nn+nn: {n_sum}')
