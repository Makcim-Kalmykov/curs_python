"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# """
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
    
n = input_number_int_positive()

list1 = []
list2 = []

temp = ""
result = 1

for i in range(1, n+1):
    result *= int(i)
    list1.append(result)

    temp += (f"{str(i)}*")
    temp_list = list(temp)
    temp_list.pop(-1)
    temp_list = "".join(temp_list)
    list2.append(temp_list)

print(list1, list2)




# $$$$$$$$       ВАРИАНТ ИЗ РАЗБОРА        $$$$$$$$$$$$


# number = int(input("Введите число: "))
# rez = []
# for i in range(1, number + 1):
#     if i > 1:
#         rez.append(i * rez[-1])
#     else:
#         rez.append(i)

# print(rez)

