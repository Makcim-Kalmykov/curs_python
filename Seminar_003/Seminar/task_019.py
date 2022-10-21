"""
Задача 19
Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
x = (A * x + B) % M
"""


# def random_my(n):
#     A = 7
#     B = 5
#     M = 11
#     x = n
#     list = []
#     for i in range(n):
#         x = (A * x + B) % M
#         list.append(x)
#     return list

# print(random_my(1))


# $$$$$$$$$$     ВАРИАНТ 2      $$$$$$$$$$$

# a = 15
# b = 21
# m = 11
# x = {}
# x[0] = 0
# x[1] = (a * x[0] + b) % m

# i = 1
# while x[i] != x[0] and i != 100:
#     x[i + 1] = (a * x[i] + b) % m
#     i += 1
# print(len(x), x.values())


# $$$$$$$$$$$$       УПРАВЯЛЕМ ПОСЛЕДОВАТЕЛЬНОСТЬЮ ПАЙТОН С ПОМОЩЬЮ seed     $$$$$$$$$$$$

import random

random.seed(10)
for i in range(10):
    print(round(random.random() * 100), end=" ")

print("--------------")                                     # генерирует одинаковую последовательность

random.seed(10)
for i in range(10):
    print(round(random.random() * 100), end=" ")


