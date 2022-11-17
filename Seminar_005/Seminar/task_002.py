"""Задача 36.
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]


test_data = [
[[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
[[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
]

for nums, exp in test_data:
assert inc_sequence(nums) == exp

[1, 5, 6, 7]
[1, 2, 3, 4, 6, 7]
"""

lst = [1, 5, 2, 3, 4, 6, 1, 7]
lst2 = [lst[0]] #lst[:1] - тоже самое
for i in lst[1:]:
    if lst[i] > lst2[-1]:
        lst2.append(lst[i])
print(lst2)

lst_2 = [lst[0]]
lst_2 = list(map(lambda i: lst[i] > lst_2[-1], range(1, len(lst))))
print(lst_2)


############ ИЗ ЗАЛА #################

test_data = [
[[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
[[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
]

# res_data = test_data[:1]
# for i in test_data[1:]:
#     if i in test_data

def cmp(acc, cur):
    if acc[-1] < cur:
        acc.append(cur)
    return acc

print(reduce(cmp, test_data[1:], test_data[:1]))