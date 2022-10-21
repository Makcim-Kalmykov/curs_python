"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
from audioop import reverse

num = int(input("Введите число: "))
temp = num
lst = []

while temp > 1:
    lst.append(temp % 2)
    temp //= 2
    if temp == 1:
        lst.append(temp)
lst.reverse()

print(f"{num} -> {lst}")
