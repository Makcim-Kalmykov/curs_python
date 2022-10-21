"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""
import math
from random import randint
from my_functions import input_number_int_positive


num = input_number_int_positive()

lst = []
lst_multiplication = []
for i in range(num):
    lst.append(randint(0, 10))

i = 0
if len(lst) % 2 == 0:
    while i <= (len(lst) - 1) / 2:
        lst_multiplication.append(lst[i] * lst[-i - 1])
        i += 1
    print(f"{lst} => {lst_multiplication}")

else:
    numb = 1
    while i < (len(lst) - 1) / 2:
        lst_multiplication.append(lst[i] * lst[-i - 1])
        i += 1 
    print(f"{lst} => {lst_multiplication} и число {lst[math.floor(len(lst)/ 2)]} (индекс {math.floor(len(lst)/ 2)}) без пары")

    
