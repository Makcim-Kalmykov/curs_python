"""
 Написать программу, которая принимает на вход два целых числа и проверяет, является ли одно число квадратом другого.
Примеры
5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет
"""


# a = int(input('введите число а: '))
# b = int(input('введите число b: '))

#                                     $$$ Вариант 1 $$$

# if a == b*b:
#     print(f'чисо b({b}) является квадратом числа а({a})')
# elif b == a*a:
#     print(f'чисо a({a}) является квадратом числа b({b})')
# else:
#     print('Числа a и b не являются квадратами')

#                                     $$$ Вариант 2 $$$

# if a == b**2 or b == a**2:
#     print('Числа являются квадратами')
# else:
#     print('Числа являются квадратами')

#                                     $$$ Вариант из зала с проверкой $$$

# a = input("a: ")
# while not a.isdigit():
#     a = input("a: ")

#                                     $$$ Варинат из зала 2 $$$

# otwet='Да'
# print(otwet if num1**2 == num2 or num2**2 == num1 else "Нет")


"""
Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
Примеры:
1, 4, 8, 7, 5 -> 8
78, 55, 36, 90, 2 -> 90
"""


#           $$$ ввод даннхы в список пример 1 $$$

# def inputIntList (len):
#     list = []
#     for i in range(len):
#         list.append(int(input(f"введите {i+1} число: ")))
#     return list

# l = inputIntList(5)
# print(l)

#                $$$ ВАРИАНТ 2 $$$$$$

# temp = []
# for i in range(1, 6):
#     text = f"Введите {i} число: "
#     temp.append(int(input(text)))

# print(f"{temp}  -> {max(temp)}") # поиск максимального значения в списке temp


#                $$$ ВАРИАНТ 3 $$$$$$

# list = [12, 41, 87, 7, 5]
# max = list[0]
# for i in range(1, len(list)):  #начинаем перебор со второго элемента
#     if max < list[i]:
#         max = list[i]
# print(max)


"""
Задача 3.
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
Примеры:
5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""

# num = int(input('Введите число: '))
# print(list(range(-num, num+1)))


#        $$$  ВАРИАНТ ИЗ ЗАЛА  $$$

# num=int(input("Введите число: "))
# r = range(-num, num+1)
# for i in r:
#     print(i)


"""
Задача 4: 
Напишите программу, которая принимает на вход число и проверяет,
кратно ли оно 5 и 10 или 15, но не 30"""

# num=int(input("Введите число: "))
# if num % 5 == 0 and num % 10 == 0 and num % 30 != 0:
#     print (True)
# elif num % 15 == 0 and num % 30 != 0:
#     print (True)
# else:
#     print(False)

#  $$$ ВАРИАНТ 2 $$$$

# num=int(input("Введите число: "))
# if num%5==0 and num%10==0 and num%30!=0 or num%15==0 and num%30!=0:
#     print (True)
# else:
#     print(False)

# $$$ ВАРИАНТ 3 $$$

# num=int(input("Введите число: "))
# print (num%5==0 and num%10==0 and num%30!=0 or num%15==0 and num%30!=0)


# def isMultOf(num, dev):
#     if num % dev == 0:
#         return True
#     else:
#         return False


# if isMultOf(a, 5) and isMultOf(a, 10) or isMultOf(a, 15) and not isMultOf(a, 30):
#     print("Ok")
# else:
#     print("No ok")


"""
Задача 5:
Напишите программу, которая будет принимать
на вход дроби и показывать первую цифру дробной части числа
6.75 -> 7
5 -> нет 
0.34 -> 3

"""

# num = float (input("Введите число: "))
# result = (num * 10) % 10
# if result != 0:
#     print (int(result))
# else: 
#     print("нет")


#           $$$ Вариант 2 $$$

# num = float(input("Введите число: "))
# num=int(num*10)
# print(num%10)





