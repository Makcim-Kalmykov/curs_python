def input_number_float():                       # ввод вещественного числа
    temp = False
    while temp == False:
        try:
            number = float(input("Введите число: "))
            temp = True
        except ValueError:
            print("ERROR: Введено не число")
    return number


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


def sum_float(num):                             # сумма цифр float
    number = list(str(num))
    number.remove(".")
    number.remove("-")

    temp = 0
    for i in number:
        temp += int(i)
    return temp



