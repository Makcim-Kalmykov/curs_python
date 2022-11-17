"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

"""

from my_functions import input_number_int_positive, list_multipliers

num = input_number_int_positive()
print(f"Cписок простых множителей числа {num} = {list_multipliers(num)}")