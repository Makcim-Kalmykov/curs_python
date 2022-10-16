"""
Задача 11.
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
Пример:
Для N = 5: 1, -3, 9, -27, 81

"""
#             # $$$$$ Вариант 1 $$$$$
# num = int(input("Введите число "))
# for i in range(num):
#     print((-3) ** i, end= " ")


# from unittest import result


# n = int(input("Введите число "))

# def sequence (num):
#     result = []
#     for i in range(num):
#         print.append((-3) ** i)
#     return result

# r = sequence(n)
# print(r)


"""
Задача 12
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Пример:
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

"""

# slovar = {}
# n = 6
# for i in range(1, n+1):
#     slovar[i] = 3 * i + 1
# print(slovar)
# assert slovar == {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}  # ПРОВЕРКА


"""
Задача 13
Напишите программу, в которой пользователь будет задавать две строки, а программа - 
определять количество вхождений одной строки в другой.
Пример:
"hello or world", "or" -> 2

"""
# x = input("Введите сторку 1: ")
# y = input("Введите сторку 2: ")
# count = 0

# for i in range(len(x) - len(y) + 1): # перебираем не все симолы, а от начала и до конца за минусом длинны второй строки 
#     temp = x[i : i + len(y)] # присваиваем временной пееменной значение  от i + длинна второй строки
#     if temp == y:
#         count += 1

# print(count)


# $$$$$ ВАРИАНТ 2 $$$$$

# text = "hello or world"
# find = "or"

# count = 0
# for i in range(len(text)): # от 0 до длинны текста
#     if text[i : i + len(find)] == find:
#         count += 1
# print(f'"{text}", "{find}" -> {count}')


# $$$$$$$$ ДЕЛАЕМ ТЕСТИРОВАНИЕ $$$$$$$$$

def count_sub(text, find):
    count = 0
    for i in range(len(text)): # от 0 до длинны текста
        if text[i : i + len(find)] == find:
            count += 1
    return count

assert count_sub("Hello or world", "or") == 3
assert count_sub("aaaaaa", "aa") == 5
assert count_sub("abababa", "aba") == 3
assert count_sub("abababa", "x") == 0

# КОРТЕЖ ТЕСТОВ
data_test [ # - двумерный список. Можно оращатся по индексу к элементам data_test[0] -> ["Hello or world", "or", 3]
    ["Hello or world", "or", 3], # можно оратиться внутри второго списка data_test[0][1] -> 'or'
    ["aaaaaa", "aa", 5],
    ["abababa", "aba", 3]
    ["abababa", "x", 0]
]

# берем список data_test и тестируем его. Если все ок, то ошибок не будет
for txt, sus_str, exept in data_test: # теест; такст который ищем; что ожидаем;
    assert count_sub(txt, sus_str) == exept, f"exept {exept}"