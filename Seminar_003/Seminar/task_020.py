"""
Задача 20
Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
Пример:
["qwe", "asd", "12", "qwe", "2"], 2 -> True
["qwe", "asd", "qwe", "681"], 7 -> False
["qwe", "asd", "qwe", "0"], 0 -> True

"""


x = ["qwe", "asd", "12", "qwe", "2"]
found = 7
print((f"{x}, {found} ->"), (f"{x}, {found} ->" in x ))



# $$$$$       ВАРИАНТ ИЗ ЗАЛА        $$$$$

# def find_num(number, my_list):
#     for item in my_list:
#         if number in item:
#             result = True
#     return False

# print(find_num(str(2), ['bag', 'car', 'phone', 'table', '2']))



# $$$$$       ВАРИАНТ ИЗ ЗАЛА        $$$$$

# print("2" in "".join(['bag', 'car', 'phone', 'table', '2']))


# $$$$$       ВАРИАНТ ИЗ ЗАЛА        $$$$$

# def is_num_present (l, n):
#     if str(n) in l:
#         return True

#     return False

# print(is_num_present(["kjhkj", "kjshd", "3"], 2))

