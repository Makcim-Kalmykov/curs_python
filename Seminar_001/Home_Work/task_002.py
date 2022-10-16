"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

"""
# $$$$$ ВАРИАНТ 1 $$$$$

# import random
# x = random.randint(0, 1)
# y = random.randint(0, 1)
# z = random.randint(0, 1)
# print("x y z")
# print(x, y, z)
# print(not(x or y or z))==(not x and not y and not z)



# $$$$$ ВАРИАНТ 2 $$$$$

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)