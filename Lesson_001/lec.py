# print('Привет мир!')

# типы данных int, float, boolean, str, list, None и т.д.

# value = None
# print(type(value))
# a = 123
# b = 1.23
# c = 'привет'

# # print (a, b, c)
# print(a, '-', b, '-', c)
# print('{} - {} - {}'.format(a, b, c))
# print('{1} - {2} - {0}'.format(a, b, c))
# print(f'{a} - {b} - {c}')

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# value = 123456
# print(value)
# print(type(value))

# ads = 'привет'
# print(ads) #вывод строки

# s = 'Привет " мир ' # s = "Привет ' мир" или s = 'Привет \' мир ' - так можно использоват ковычки внутри строки
# print(s)                                               # \n - переход на новую строку

# f = True
# print(f)
# d = False
# print(d)


# list = []
# print(list)

# list1 = [1, 2, 3]
# print(list1)

# list2 = [1, 2.343, 'текст', False, True] #так лучше не делать. Делать хранилище данных одного типа
# print(list2)


# print('Введите а:')
# a = input()
# print('Введите b:')
# b = input()
# print(a,b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# если а = 10 и b = 20 то print(a,' + ', b, " = ", a + b) = 1020  (по умолчанию работаем со строками нужно сделать так):

# print('Введите а:')
# a = int(input())
# # a = float(input()) - если нужно вещественное и т.д.
# print('Введите b:')
# b = int(input())
# print(a,b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print(a,' + ', b, " = ", a + b)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$   АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ   $$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# +, -, *, %, //, **

# приоритет операций: **, унарный плюс, унарный минус, *, /, //, %, +, -
# () скобки меняют приоритет

# a = +2 # унарный плюс
# b = -321 # унарный минус(класическая инверсия числа)
# c = a + b
# print(c)


# a = 12
# b = 8
# c = a / b # по умолчанию работает как для вещественных чисел
# print(c)
# d = a//b # деление в целых числах
# print(d)
# e = a % b
# print(e)
# f = a ** b # возведение в степень
# print(f)


# a = 1.3
# b = 3
# c = a * b
# print(c) # ожидаем получить 3.9, но получаем 3.9000000000000004
# # чтобы избежать:
# a = 1.32134
# b = 3
# c = round(a * b) # если аргументов нет, то округление по математическим правилам до целого
# print(c)
# c = round(a * b, 3) # 3 знака после запятой
# print(c)


# a = 3
# a = a + 5
# print(a)
# # можно написать по другому
# b = 3
# b += 5
# print(b)



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$   ЛОГИЧЕСКИЕ ОПЕРАЦИИ   $$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# a = 1 > 4
# print(a) #результат False

# a = 1 < 4 
# print(a) # результат истина

# a = 1 < 4 and 5 > 2 
# print(a)

# a = 1 == 2
# print(a)

# a = 'qwer'
# b = 'qwer'
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# a = 1 < 3 < 5 < 10 < 20
# print(a)

# b = 1
# c = 4
# x = 123
# print(b < c > x)


# f = 1 > 2 or 4 < 6 # 1 больше 2 ИЛИ 4 меньше 6
# print(f)

from operator import is_


# a = [1, 2, 3, 4]
# print(a)
# print(2 in a) # поучаем истину, потому что 2 содержится в списке
# print(not 2 in a)
# is_odd = a[0] % 2 == 0 # is_odd = not a[0] % 2 - тоже самое #ПРОВЕРКА НА ЧЕТНОСТЬ 
# print(is_odd)


# $$$$$$$   Управляющие конструкции if, if-else   $$$$$$$$$$$$

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# if условие:
#     оператор
# elif условие:
#     оператор
# elif условие:
#     оператор
# else:
#     оператор


# $$$$$     Wile     $$$$$$
# переворачиваем число
# a = 23
# invert = 0
# while a != 0:
#     invert = invert * 10 + (a % 10)
#     a //= 10
# print(invert)


# $$$$$     Wile + else     $$$$$$
# a = 23
# invert = 0
# while a != 0:
#     invert = invert * 10 + (a % 10)
#     a //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(invert)



# $$$$$     for     $$$$$$

# for i in enumeration: # i - счетчик, enumeration - энумерируемый объект, например список
#     оператор 1
#     оператор 2
#     оператор 3

# for i in 1,2,3,4,5:
#     print(i**2)


# list = [1,2,33,4,5]
# for i in list:
    # print(i)


# list = range(10)
# for i in list:
#     print(i)


# # тоже самое
# for i in range(10): # от 0 до 9
#     print(i)


# for i in range(1, 10, 2): # от 1 до 10 с прирожение по 2
#     print(i)


for i in 'qwerty':
    print(i)