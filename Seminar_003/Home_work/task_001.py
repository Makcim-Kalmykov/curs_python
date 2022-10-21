"""nu
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""

from random import randint, random
from my_functions import input_number_int_positive

num = input_number_int_positive()
list = []
lst1 = []

for i in range(num):
    list.append(randint(0, 10))
    if i % 2 != 0:
        lst1.append(list[i])

print(f"{list} -> на нечётных позициях элементы {lst1}, ответ: {sum(lst1)}")
