"""
Задача 21
Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1

"""

# def found(list, found):
#     count = 0
#     temp = - 1
#     i = 0
#     while i < len(list):
#         if found in str(list[i]):
#             count += 1
#         if count == 2:
#             temp = i
#         i += 1
#     return temp

#     print(f"{list}, ищем: '{found}', ответ: {temp}")

# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# fou = "qwe"
# print(f"{lst}, ищем: '{fou}', ответ: {found(lst, fou)}")




# $$$$$       ВАРИАНТ ИЗ ЗАЛА        $$$$$

# def is_index(lst, t):
#     count = -1
#     for i in range(0, len(lst)):
#         if lst[i] in t:
#             count = i
#         return count



# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# text = "йцу"
# print(is_index(my_list, text))




# $$$$$       ВАРИАНТ ИЗ ЗАЛА        $$$$$

def find_num(number, my_list, pos_count = 2):       # pos_count - кол-во вхождений - параметр по умолчанию
    num = 0
    for i, item in enumerate(my_list):
        if item == number:
            num += 1
            if num == pos_count:
                return i
    return -1

print(find_num("йцу", ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]))
