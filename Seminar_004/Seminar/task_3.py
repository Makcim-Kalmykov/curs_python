"""
Задайте 2 числа и напишите программу, 
которая найдет НОК (наименьшее общее кратное) этих двух чисел.
"""


# def delitel(a, b):
#     min_num = min (a, b)
#     for i in range(1, min_num + 1):
#         if ((a % i == 0) and (b % i == 0)):
#             temp = i
#     return temp


# def find_(a, b):
#     return (a * b / delitel(a, b))

# print(find_(126, 70))



########## ВАРИАНТ ИЗ ЗАЛА #############
def find_NOK (a, b: float):
    delitel = min (a, b)
    while delitel > 2:
        if a % delitel == 0 and b % delitel == 0:
            print (delitel)
            break
        delitel /= 2
    return (a * b) / delitel
print(find_NOK(16, 20))