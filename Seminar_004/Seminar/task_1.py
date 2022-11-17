"""
Задача 27
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел.

Пример
"12 346 62 34 9 25623 42 34" -> 25623, 9

test_data = [
["12 346 62 34 9 25623 42 34", [25623, 9]],
["7 346 1 34 9 6 42 -2 6", [346, -2]],
]

for nums, expected in test_data:
assert find_max_min(map(int, nums.split(" "))) == expected

"""

# $$$$$$$$$$$$$$    МОЙ ВАРИАНТ   $$$$$$$$$$$$$$$$

# str = "12 346 62 34 9 25623 42 34"
# lst = list(map(int, str.split()))
# print(f"{max(lst)}, {min(lst)}")




# $$$$$$$$$$$$$$    ВАРИАНТ ИЗ ЗАЛА  $$$$$$$$$$$$$$$$

def find_max_min(my_lst):
    max_min_lst = []
    min_num = int(my_lst[0])
    max_num = int(my_lst[0])

    for i in my_lst:
        if int(i) < min_num:
            min_num = int(i)
        elif int(i) > max_num:
            max_num = int(i)
    max_min_lst.append(max_num)
    max_min_lst.append(min_num)
    return max_min_lst


# num_str = '12 346 62 34 9 25623 42 34'
# num_lst = num_str.split(' ')
# find_max_min(num_lst)



test_data = [
["12 346 62 34 9 25623 42 34", [25623, 9]],
["7 346 1 34 9 6 42 -2 6", [346, -2]],
]

for nums, expected in test_data:
    assert find_max_min(list(map(int, nums.split(" ")))) == expected