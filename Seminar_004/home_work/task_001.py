"""
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from cmath import pi

num = int(input("Задайте необходимую точность числа Пи: "))

print(f"Число Пи с точностью {num} = {round(pi, num)}")