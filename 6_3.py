# Решение через функцию title()
def ext_func1(words):
    """ Переводит строку из слов, начинающихся с маленькой буквы, в слова, начинающиеся с большой буквы.

    words -- введенная пользователем строка (str)
    возвращает str
    """
    new_str = words.split()
    final_str = []

    def int_func1(word):
        """ Переводит слово, введенное с маленькой буквы, в слово, введенное с большой буквы.

        word -- введенное пользователем слово (str)
        возвращает str
        """
        return word.title()

    for i in new_str:
        final_str.append(int_func1(i))

    return " ".join(final_str)


# Решение через функции сhr() и ord()
def ext_func2(words):
    """ Переводит строку из слов, начинающихся с маленькой буквы, в слова, начинающиеся с большой буквы.

    words -- введенная пользователем строка (str)
    возвращает str
    """
    new_str = words.split()
    final_str = []

    def int_func2(word):
        """ Переводит слово, введенное с маленькой буквы, в слово, введенное с большой буквы.

        word -- введенное пользователем слово (str)
        возвращает str
        """
        letter_capitalized = chr(ord(word[0]) - ord('a') + ord('A'))
        return letter_capitalized + word[1:]

    for i in new_str:
        final_str.append(int_func2(i))

    return " ".join(final_str)


my_words = input('Введите слова, разделенные пробелами: ')
print(ext_func1(my_words))
print(ext_func2(my_words))
