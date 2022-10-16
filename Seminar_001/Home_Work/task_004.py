"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""

def ImputNumber():
    num = ""
    temp = False
    while temp == False:
        while num.isnumeric() == False:
            try:
                num = int(input(f"Введите номер четверти декартовой системы координат: "))
                break
            except ValueError:
                print("Неверный ввод")
                continue
        num = int(num)
        if (num < 1 or num > 4):
            print("Введеное число не является номером четверти")
            num = ""
        else:
            temp = True
    return num   

a = ImputNumber()
rangeNumb = ["[x > 0; y > 0]", "[x < 0; y > 0]", "[x < 0; y < 0]", "[x > 0; y < 0]"]
print(f"Диапазон возможных координатов точек в {a} четверти: {rangeNumb[a - 1]}")
  