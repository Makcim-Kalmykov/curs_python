"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
"""

from random import randint

def input_number_int_positive():                # ввод целого числа больше 0
    num = ""
    temp = False
    while temp == False:
        while num.isnumeric() == False:
            try:
                num = int(input(f"Введите целое число больше 0: "))
                break
            except ValueError:
                print("Неверный ввод")
                continue
        num = int(num)
        if (num == 0 or num < 0):
            print("Введеное число меньше или равно 0")
            num = ""
        else:
            temp = True
    return num

num = input_number_int_positive()

list1 = []
for i in range(num):
    list1.append(randint(-num, num))

print(f"Список из {num} элемментов из промежутка [{-num}, {num}]: {list1}")

list2 = []
with open("file_2.txt", "r") as file:
    for line in file:
        list2.append(int(line))

print(f"Позиции элементов для перемножения из файла file_2.txt: {list2}")

result = 1
temp = ""

for i in range(0, len(list2)):
    if list2[i] <= len(list1) - 1:
        result *= list1[list2[i]]
        temp += f"{list1[list2[i]]}*"

print(f"Результат произведения {temp[:-1]} = {result}")
