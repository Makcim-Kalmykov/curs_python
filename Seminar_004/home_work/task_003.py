"""
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

"""
from my_functions import input_number_int_positive
from random import randint

print("Введите желаемую длинну последовательности чисел")

num = input_number_int_positive()

lst = [randint(1, 10) for i in range(1, num + 1)]
print(f"Исходная последовательность -> {lst}")

lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(f"Cписок неповторяющихся элементов исходной последовательности {lst2}") 


