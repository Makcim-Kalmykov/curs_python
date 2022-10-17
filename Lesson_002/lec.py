
# $$$$$$$$$ РАБОТА С ФАЙЛАМИ $$$$$$$$$$$$$$


# colors = ["red", "green", "blue"]
# data = open("file.txt", "w") # создаем текстовую переменную и связываем ее с файлом. Указ путь к файлу и мод для работы
# data.writelines(colors) # разделителей не будет Записываем список colors в файл

# data.write("\nLine 2\n")
# data.write("\nLine 3\n")

# data.close()  # ЗАКРЫТИЕ СВЯЗИ И ФАЙЛА

# $$$$$$$ ПО ДРУГОМУ $$$$$$$$$$$$

# with open("file.txt", "a") as data:
#     data.write("Line 2\n")
#     data.write("Line 3\n")        # РАЗРЫВ СВЯЗИ ПРОИСХОДИТ САМОСТОЯТЕЛЬНО !!!!!!!



# path = "file.txt"   #СОЗДАЕМ ПУТЬ К ПАПКЕ 
# data = open(path, "r")   # ОТКРЫВАЕМ В РЕЖИМЕ ЧТЕНИЯ
# for line in data:
#     print(line)
# data.close()

# exit()


# import hello         # ИМПОРТ ФУНКЦИИ ИЗ ФАЙЛА hello.py
# print(hello.f(1))    # функция f(x) из файла hello.py 


# import hello as h    # ЧТОБЫ НЕ ПИСАТЬ ПОСТОЯННО hello
# print(h.f(1))        # функция f(x) из файла hello.py 




# $$$$$$$$$ МЕТОДЫ $$$$$$$$$$$$$


# def new_string(symbol, count):
#     return symbol * count      # в python можно перемножать строку на число

# print(new_string("!", 5))     # -> !!!!!
# print(new_string("!")) # -> будет ошибка. Если записать def new_string(symbol, count = 3) ошибки не будет  -> !!!
# print(new_string(4))   # -> 12     (4*3)  count=3



# def contan (*params):
#     res: str = ""      # переменная res с типом данных str
#     for item in params:
#         res += item
#     return res

# print(contan("a", "b", "c", "d", "w"))   # -> abcw
# print(contan("a", "1", "b", "2"))        # -> a1b2
# print(contan(1, 2, 3, 4))    # -> полусим ошибку, потому что логина работает со строкой  



                        # РЕКУРСИЯ 



# def fib(n):            #  ЧИСЛА ФИБОНАЧИ
#     if n in [1, 2]:    #  УСЛОВИЯ ДЛЯ ВЫХОДА
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))

# print(list)




# $$$$$$$    КОРТЕЖИ       $$$$$$$$$$$



# a = (3, 1, 2, 4)
# print(a)
# print(a[0])  # -> 3
# print(a[-1]) # -> 4
# # a = (2,) - кортеж из одного числа
# for item in a:
#     print(item)





# $$$$$$   СЛОВАРИ   $$$$$$$$$



# direct = {}
# direct = \
#     {
#     "up": "вверх",
#     "left": "влево",
#     "rigth": "вправо"
#     }

# print(direct)
# print(direct["left"])


# for k in direct.keys():     # цикл по ключам 
#     print(k)              # распечатать ключи

# for k in direct.values():     # цикл по значениям 
#     print(k)                # распечатать значения


# for k in direct:     # цикл по значениям 
#     print(k)         # -> up 
#                      #    left
#                      #    rigth


# for k in direct:     # цикл по значениям 
#     print(direct[k]) # -> вверх
#                      #    влево
#                      #    вправо

# direct["up"] = "up"     # присвоение нового значения
# print(direct["up"])

# del direct["left"]      # удаление элемента

# for item in direct:     # for (k,v) in direct.items():
#     print("{}: {}".format(item, direct[item]))      # -> up: вверх
#                                                     # -> left: влево
#                                                     # -> rigth: вправо




# $$$$$$$$$$$   МНОЖЕСТВА   $$$$$$$$$$



# colors = {"red", "green", "blue"}       # тип даннхы set
# print(colors)                           # -> {'red', 'green', 'blue'}

# colors.add("grey")                      # добавление элемента
# print(colors)                           # -> {'grey', 'red', 'green', 'blue'}

# colors.remove("red")                    # удаление из множества "red"
# print(colors)                           # -> {'green', 'blue', 'grey'}

# # colors.remove("bldck")    -> KeyError: 'black'  удаление несуществующего элемента

# colors.discard("red")                   # удаление из множества "red", если его нет, то ошибки не будет

# colors.clear()                          # -> {}    очистка множества



# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy()                            # c = {1, 2, 3, 5, 8}               КОПИСРОВАНИЕ МНОЖЕСТВА

# u = a.union(b)                          # u = {1, 2, 3, 5, 8, 13, 21}       ОБЪЕДИНЕНИЕ МНОЖЕСТВ

# x = {1, 2, 3}  
# y = {4, 5, 6}  
# z = {7, 8, 9}
# output = x.union(y, z)
# print(output)                           # -> {1, 2, 3, 4, 6, 7, 9}

# i = a.intersection(b)                   # i = {8, 2, 5}                     ПЕРЕСЕЧЕНИЕ МНОЖЕСТВ

# x = {1, 2, 3}  
# y = {4, 3, 6}                           # через &
# print(x & y)                            # -> {3}

# x = {1, 2, 3}  
# y = {4, 3, 6}
# z = x.intersection(y)                   # черех .intersection
# print(z)                                # -> {3}   тоже самое 



# dl = a.difference(b)                    # dl = {1, 3}                       РАЗНИЦА МЕЖДУ МНОЖЕСТВАМИ
# dr = b.difference(a)                    # dr = {13, 21}

# set_a = {1, 2, 3, 4, 5}  
# set_b = {4, 5, 6, 7, 8}  
# diff_set = set_a.difference(set_b)      # через .difference
# print(diff_set)                         # -> {1, 2, 3}

# set_a = {1, 2, 3, 4, 5}  
# set_b = {4, 5, 6, 7, 8}                 # через - (минус)
# print(set_a - set_b)                    # -> {1, 2, 3}



# et_a = {1, 2, 3, 4, 5}                 #                                    СИММЕТРИЧНАЯ РАЗНИЦА  
# set_b = {4, 5, 6, 7, 8}  
# symm_diff = set_a.symmetric_difference(set_b)  
# print(symm_diff)                        # -> {1, 2, 3, 6, 7, 8}

# set_a = {1, 2, 3, 4, 5}  
# set_b = {4, 5, 6, 7, 8}                 # через ^ 
# print(set_a ^ set_b)                    # -> {1, 2, 3, 6, 7, 8}


# q = a \
#     .union(b) \
#     .difference(a.intersection(b))      # -> {1, 21, 3, 13}



# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])  # множество из списка
# print("May" in months)                  # -> True                           проверка наличия May в множестве

# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# print("Nicholas" in months)             # -> False


# s = frozenset(a)                          #                                 ЗАМОРОЗКА МНОЖЕСТВА



# $$$$$$$$      СПИСКИ      $$$$$$$$$$$$


# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)                # 1 2 3 4 5 

# print()                                     # печатаем пустую строку

# for e in list2:
#     print(e)                # 1 2 3 4 5

# list1[0] = 123
# list2[1] = 321

# for e in list1:             
#     print(e)                # 123 321 3 4 5

# for e in list2:                         
#     print(e)                # 123 321 3 4 5



# list1 = [1, 2, 3, 4, 5]

# print(len(list1))               # -> 5 (длинна списка)
# print(list1)                    # -> [1, 2, 3, 4, 5]
# print(list1.pop())              # .pop - показывает последний элемент списка и удаляет его
# print(list1)                    # -> [1, 2, 3, 4]

# print(len(list1))               # 4
# print(list1.pop())              # 4
# print(list1)                    # [1, 2, 3]

# print(len(list1))               # 3
# print(list1.pop())              # 3
# print(list1)                    # [1, 2]

# print(len(list1))               # 2
# print(list1.pop())              # 2
# print(list1)                    # [1]
# print(len(list1))               # 1


list1 = [1, 2, 3, 4, 5]
print(list1.pop(2))                 # 3 -> удаление элемента с индексом 2
print(list1)                        # -> [1, 2, 4, 5]

print(list1.insert(3, 13))          # добавляем 13 на элемент с индексом 3
print(list1)                        # -> [1, 2, 4, 13, 5]

print(list1.append(323))            # добавляем 323 в конец списка
print(list1)                        # -> [1, 2, 4, 13, 5, 323]
