"""
Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

Пример:
- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }

"""

def input_number_int_positive():                      # ввод целого числа больше 0
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
    
number = input_number_int_positive()

list = {}
for i in range(1, number + 1):
    list[i] = f"{round((1 + 1 / i)**i, 2)}"

print(f" n = {number}: {list}")