"""
Задача 38.
Напишите программу, удаляющую из текста все слова, содержащие "абв".


test_data = [
[["привет абв как абвышные дела?", "абв"], "привет как дела?"]
]
for args, exp in test_data:
assert remove_substr(*args) == exp
#assert remove_substr_func(*args) == exp

"""

# def delete_text(lst_text, find):
#     text_join = " ".join(lst_text)                  # склеиваем список в строку
#     temp = text_join.split(" ")                     # разбиваем строку на список слов
#     lst = []
#     for i in temp:
#         if find not in i:                           # ищем в списке слов необходимые стволы
#             lst.append(i)
#     temp = ' '. join(lst)                           # склеиваем новый список в строку
#     return temp


# text_new = ["привет абв как абвышные дела?", "абв"]
# find_text = "абв"
# print(delete_text(text_new, find_text))





###################""" ВАРИВЕТ ИЗ ЗАЛА """####################

test_data = "привет абв как абвышные дела?"
remove_set = "абв"

# test_list = test_data.split()
# res_data = []
# for i in test_list:
#     if remove_set not in i:
#         res_data.append(i)

# print(' '.join(res_data))


############## через split ############

test_list = test_data.split()
print(" ".join([i for i in test_list if "абв" not in i ]))


test_list1 = test_data.split()
print(" ".join(filter(lambda i: "абв" not in i, test_list1)))
