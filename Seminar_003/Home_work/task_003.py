"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

from random import randint, random
from my_functions import input_number_int_positive

num = input_number_int_positive()

lst = []
lst2 = []

for i in range(num):
    lst.append(round(random(), 2))
    lst2.append(randint(0, 10))

c = [round(lst[i]) + lst2[i] for i in range(len(lst))]

print(f"{c} => разница между максимальным и минимальным значением дробной части {max(lst) - min(lst)}")