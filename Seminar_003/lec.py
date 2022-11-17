# $$$$$$$$       ФОРМАТИРОВАНИЕ        $$$$$$$$$$$$

# num = 4
# pi = 3.14434
# print(f"pi: {pi} number: {num}")
# print("pi: {:.2f} number: {}".format(pi, num))              # :.2f - вывести число с плавающей точкой и округлить до 2-х знаков
# print("pi: {:10.2f} number: {}".format(pi, num))            # добавили пространство перед
# print("pi: {:<10.2f} number: {}".format(pi, num))           # добавили пространство после
# print(f"pi: {pi:<10.2f} number: {num}")                     # аналог .format 







# $$$$$$$$       ЧТЕНИЕ ИЗ ФАЙЛА        $$$$$$$$$$$$

# f = open("name_files", "w", encoding="utf-8")                   # создание файла с режимом 'w' - на запись с кодировкой UTF-8
# f.write("Hello world\nsome string")                             # создаем запис в файле;  \n - символ переноса строки (будет 2 строки)
# f.flush()                                                       # принудителная запись на диск
# f.close()                                                       # закрытие файла

# f = open("name_files", "a", encoding="utf-8")                   # a - режим добавления данных
# f.write("\n123465")

# f = open("name_files", "r", encoding="utf-8")                   # r - режим чтения данных
# print(f.read(5))                                                # read - чтение данных. 5 - кол-во сиволов для чтения
# f.seek(0)                                                       # seek - управление курсором. 0 - в начало файла
# f.close()

# f = open("name_files", "r", encoding="utf-8")
# for line in f:                                                  # чтение файла по строчно
#     print(line)                                                 # печать построчно
# f.close()

f = open("name_files", "rb")                                    # открытие в бинарном режиме
print(f.read())                                                 # -> b'Hello world\r\nsome string\r\n123465'