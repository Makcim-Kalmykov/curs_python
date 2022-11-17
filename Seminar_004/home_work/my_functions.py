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


def fib(n):                                     #  ЧИСЛА ФИБОНАЧИ
    if n in [1, 2]:    
        return 1
    if n in [0]:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


def list_multipliers(a):                        #  РАЗЛОЖЕНИЕ ЧИСЛА НА ПРОСТЫЕ МНОЖИТЕЛИ 
    lst = []
    i = 2
    while a > 1:
        if a % i == 0:
            lst.append(i)
            a = a / i
            i = 2
        else: 
            i += 1
    return lst

