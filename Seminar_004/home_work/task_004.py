"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

"""

import random
from my_functions import input_number_int_positive

print("Введите натуральную степень k")
k = input_number_int_positive()
min_coefficient = 0
max_coefficient = 100

lst = [random.randint(min_coefficient, max_coefficient + 1) for i in range(k + 1)]
lst = lst[::-1]

stroka = ''
if len(lst) < 1:
    stroka = 'x = 0'
else:
    for i in range(len(lst)):
        if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
            stroka += (f'{lst[i]}x^{len(lst) - i - 1}')
            if lst[i + 1] != 0:
                stroka += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            stroka += (f'{lst[i]}x')
            if lst[i + 1] != 0:
                stroka += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            stroka += (f'{lst[i]} = 0')
        elif i == len(lst) - 1 and lst[i] == 0:
            stroka += ' = 0'
print(stroka)

with open('task_004.txt', 'w') as data:
    data.write(stroka)