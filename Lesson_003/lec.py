
# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def cal(x):
#     return x + 10

# def cal2(x):
#     return x * 10

# def math(op, x):                         # берем на вход операцию и число
#     print(op(x))

# math(cal2, 10)
# math(cal, 10)


# def sum (x, y):
#     return x + y

# sum = lambda x, y: x + y          # тоже самое что функция sum(x, y)

# f = sum

# def mult (x, y):
#     return x * y

# def cal (op, a, b):
#     print(op(a, b))
#     return op(a, b)

# cal(mult, 4, 5)
# cal(f, 4, 5)                            # тоже самое
# cal(sum, 4, 5)                          # тоже самое
# cal(lambda x, y: x + y, 4, 5)           # тоже самое


"""
# $$$$$$$$        List Comprehension          $$$$$$$$$             ДЛЯ БЫСТРОГО СОЗДАНИЯ СПИСКОВ
"""

# list = []                                       # создание списка от 1 до 20
# for i in range(1, 21):
#     list.append(i)
# print(list)


# lst = [i for i in range(1, 21)]                 # создание списка от 1 до 20
# print(lst)


# list = []                                       # список четных числе от 1 до 20
# for i in range(1, 21):
#     if (i % 2 == 0):
#         list.append(i)
# print(list)

# lst = [i for i in range(1, 21) if i % 2 == 0]                 # список четных числе от 1 до 20
# print(lst)


# lst = [(i, i) for i in range(1, 21) if i % 2 == 0]            # список КОРТЕЖЕЙ четных числе от 1 до 20
# print(lst)


# def f(x):
#     return x**3                        #возводим в 3 степень

# lst = [f(i) for i in range(1, 21) if i % 2 == 0]       # передаем ф-ию f(x) -> [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]
# # берем список от 1 до 20, выбираем только четные, затем к ним применяем ф-ию f(x) - возводим в 3 степень
# print(lst)

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]      # подкючаем кортеж. Будет число и его куб
# print(list)           #[(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]


"""
ЗАДАЧА: В файле хранятся числа, нужно выбрать четные и составить списорк пар(число; квадрат числа)

Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)] 

"""

# pach ='/User/python/...'                                    # путь к файлу
# f = open (pach, "r", encoding="utf-8")                      # связываем переменную с файлом на диске
# data = f.read() + ""                                        # считываем все что есть в строке и искусственно добавляем пробел
# f.close()                                                   # закрываем файл

# list = []

# while data != "":                           # пробегаемся по свей строке, которую считали выше. Проверка - пока строка не пустая
#     space_pos = data.index(" ")             # находим перкую позицию пробела. Берем все что от позиции 1 симола, до позиции пробела
#     list.append(int(data[:space_pos]))      # Превратить это в число и добавить в список
#     data = data[:space_pos + 1:]            # обновляем строку откинув то, что уже нашли

# lst = []
# for e in list:
#     if not e % 2:                           # проверка что число четное
#         lst.append((e, e**2))               # доюавляем в новый список кортежи

# print(lst)


# $$$$$$     ДЕЛАЕМ КОД ЛУЧШЕ     $$$$$$$

# def select(f, col):                         # фунция select принимает в арг функцию и набор данных
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()         # на выходе получим набор строк

# res = select(int, data)
# print(res)                                  # -> [1, 2, 3, 5, 8, 15, 23, 38]

# res = where(lambda x: not x%2, res)
# print(res)                                  # -> [2, 8, 38]

# res = select(lambda x:(x, x**2), res)
# print(res)                                  # -> [(2, 4), (8, 64), (38, 1444)]


"""
# $$$$$$$$ *******    ФУНКЦИЯ MAP     *********** $$$$$$$$
"""


# f(x) -> x + 10
# map(f, [1, 2, 3, 4, 5])       -> [11, 12, 13, 14, 15]     Принимает на вход ф-ию которую нужно применить к набору данных

# li = [x for x in range(1, 20)]
# print(li)                                   # ->  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# li = list(map(lambda x:x+10, li))           # делаем явное преобразование в list (в список)
# print(li)


# data = list(map(int, input().split()))      # будем получать список, который пробрасывать в map
# print(data)                                 # вводим через пробел 1 2 45 8  ->  [1, 2, 45, 8]

# a = map(int, "1 2 45 8".split())
# for i in a:
#     (print(i))                              #  1
#                                                2
#                                                45
#                                                8


# a = map(int, "1 2 3".split())
# for i in a:
#     (print(i))                              #  1
# #                                              2
# #                                              3
# print("----")                               # ---
# for i in a:
#     (print(i))                              # ничего не будет если на предыдущем этапе работу map не сохранили в список
#                                             # нужнео так    a = lsit(map(int, "1 2 3".split()))
#                                             # map - это итератор


# $$$$$$     ДЕЛАЕМ КОД  ЕЩЕ ЛУЧШЕ     $$$$$$$

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()         # на выходе получим набор строк

# res = map(int, data)
# print(res)                                  # -> [1, 2, 3, 5, 8, 15, 23, 38]

# res = where(lambda x: not x%2, res)
# print(res)                                  # -> [2, 8, 38]

# res = list(map(lambda x:(x, x**2), res))
# print(res)                                  # -> [(2, 4), (8, 64), (38, 1444)]


"""
            $$$$$$$$ *******    ФУНКЦИЯ filter     *********** $$$$$$$$

ф-ия filter() применяет указанную ф-ию к каждому элементу итерируемого объекта и возвращает итератор
с теми объектами, для которых ф-ия вернула True

f(x) -> x - четное
filtrer (f, [1, 2, 3, 4, 5])   ->    [2, 4]

НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

"""

# lst = [i for i in range(10)]
# print(lst)                                          # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = list(filter(lambda x: not x % 2, lst))
# print(res)                                          # -> [0, 2, 4, 6, 8]



# $$$$$$     ДЕЛАЕМ КОД  ЕЩЕ ЛУЧШЕ     $$$$$$$

# data = '1 2 3 5 8 15 23 38'.split()         # на выходе получим набор строк

# res = list(map(int, data))
# print(res)                                  # -> [1, 2, 3, 5, 8, 15, 23, 38]

# res = list(filter(lambda x: not x%2, res))
# print(res)                                  # -> [2, 8, 38]

# res = list(map(lambda x:(x, x**2), res))
# print(res)                                  # -> [(2, 4), (8, 64), (38, 1444)]






"""
            $$$$$$$$ *******    ФУНКЦИЯ zip     *********** $$$$$$$$

ф-ия zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

кол-во элементов в результате равно минимальному кол-ву элементов входного набора

zip ([1, 2, 3], ['о', 'г', 'т'], ['f', 's', 't'])  -> [(1, 'o', 'f'), (2, 'г', 's'), (3, 'т', 't')]

НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

"""

# user = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
# ids = [4, 5, 9 , 14, 7]

# data = list(zip(user, ids))
# print(data)                                 # -> [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]


# sal = [44, 456, 789]
# data = list(zip(user, ids, sal))
# print(data)                                 # -> [('user1', 4, 44), ('user2', 5, 456), ('user3', 9, 789)]





"""
            $$$$$$$$ *******    ФУНКЦИЯ enumerate     *********** $$$$$$$$

ф-ия enumerate() применяется к итерируемому объекту и возвращает новый генератор с кортежами из индекса и элементов
входных данных

enumerate (['Казань', 'Смоленск', 'Рыбки']
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки')]

НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

"""
user = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
ids = [4, 5, 9 , 14, 7]
sal = [44, 456, 789, 45]
data = list(enumerate(user))
print(data)                         # -> [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5'), (5, 'user6')]


data = list(enumerate((ids, sal)))
print(data)                         # -> [(0, [4, 5, 9, 14, 7]), (1, [44, 456, 789, 45])]