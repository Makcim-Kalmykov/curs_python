from random import randint, shuffle


lst = [i for i in range(10)]
print(lst)
# первый вариант
for i in range(len(lst)):
    temp = lst[i]
    r = randint(0, len(lst) - 1)        # находим рандомно позицию 
    lst[i] = r                          # меняем числа по позициям
    lst[r] = temp                       # меняем числа по позициям
print(lst)

# первый вариант
shuffle(lst)
print(lst)