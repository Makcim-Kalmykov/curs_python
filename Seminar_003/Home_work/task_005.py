"""
адайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

"""

from my_functions import fib

num = int(input("Введите число k: "))

list = []
for i in range(0, num + 1):
    list.append(fib(i))

lst = []
i = len(list) - 1
while i > 0:
    if i % 2 == 0:
        lst.append(-list[i])
    else:
        lst.append(list[i])
    i -= 1
    
print(f"Для k = {num} список будет выглядеть так: {lst + list}")