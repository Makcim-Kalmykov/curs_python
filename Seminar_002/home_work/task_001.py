"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11

"""
def input_number_float():                      # ввод вещественного числа
    temp = False
    while temp == False:
        try:
            number = float(input("Введите число: "))
            temp = True
        except ValueError:
            print("ERROR: Введено не число")
    return number


def sum_float(num):                             # сумма цифр float
    number = list(str(num))
    number.remove(".")
    number.remove("-")

    temp = 0
    for i in number:
        temp += int(i)
    return temp

number = input_number()
temp = sum_float(number)
print(f"{number} -> {temp}")
