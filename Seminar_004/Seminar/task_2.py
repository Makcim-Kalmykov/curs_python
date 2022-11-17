"""
адача 28
Найдите корни квадратного уравнения Ax² + Bx + C = 0, где A ≠ 0 двумя способами: 
1) с помощью математических формул нахождения корней квадратного уравнения 
2) с помощью дополнительных библиотек Python

test_data = [
[[1, -3, 2], [1.0, 2.0]],
[[1, 2, 1], [-1, -1]],
[[2, 2, 1], []]
]

for nums, expected in test_data:
assert quadratic_equation(*nums) == expected



"""

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        x1 = (-b + discriminant**0.5) / 2*a
        print(x1)
        return [x1]
    elif discriminant > 0:
        x1 = (-b - discriminant**0.5) / 2*a
        x2 = (-b + discriminant**0.5) / 2*a
        print(x1, x2)
        return [x1, x2]
    else: 
        print("Корней нет")
        return []



# при помощи доп библиотеки



test_data = [
[[1, -3, 2], [1.0, 2.0]],
[[1, 2, 1], [-1]],
[[2, 2, 1], []]
]

for nums, expected in test_data:
    assert quadratic_equation(*nums) == expected



