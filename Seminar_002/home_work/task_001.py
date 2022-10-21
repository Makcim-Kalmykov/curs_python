"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11

"""

# def input_number_float():                      # ввод вещественного числа
#     temp = False
#     while temp == False:
#         try:
#             number = float(input("Введите число: "))
#             temp = True
#         except ValueError:
#             print("ERROR: Введено не число")
#     return number


# def sum_float(num):                             # сумма цифр float
#     number = list(str(num))
#     number.remove(".")
#     number.remove("-")

#     temp = 0
#     for i in number:
#         temp += int(i)
#     return temp

# number = input_number()
# temp = sum_float(number)
# print(f"{number} -> {temp}")


# $$$$$$$$       ВАРИАНТ ИЗ РАЗБОРА        $$$$$$$$$$$$

# def sum_element(str_number):
#     result = 0
#     for i in range(len(str_number)):    # ["1", "2", "3"]
#         result += int(str_number[i])    # преобразуем строку в int и прибавляем в результат
#     return result

# number = float(input("Введите число: "))
# print(sum_element("".join(str(number).split("."))))   # разбиваем строку при помощи ф-ии join и отправляем в ц-ию sum_elemen 
#                                                       # элемент number как список строк: 123 -> ["1", "2", "3"]

# # вариант 2

# print(sum(map(int, "".join(str(number).split(".")))))



# $$$$$$$$$        ЕЩЕ  ВАРИАНТ          $$$$$$$$

def is_summ(text_number):                   # перебираем строку text_number
    summa = 0
    for elem in text_number:
        if elem.isdigit():     # если элемент число
            summa = summa + int(elem)       # тогда преобразуем в int и складываем
    return summa

print(is_summ('-123.4'))