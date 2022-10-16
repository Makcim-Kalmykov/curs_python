"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

"""

def ImputNumber(coord):
    num = ""
    temp = False
    while temp == False:
        while num.isnumeric() == False:
            try:
                num = int(input(f"Введите коордтнату точки по {coord} не равную 0: "))
                break
            except ValueError:
                print("Неверный ввод")
                continue
        num = int(num)
        if (num == 0):
            print("Введеное число '0'")
            num = ""
        else:
            temp = True
    return num    
    
x1 = ImputNumber('x1')
y1 = ImputNumber('y1')
x2 = ImputNumber('x2')
y2 = ImputNumber('y2')

result = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 3)
print(f"Расстояние между точкой А({x1, y1}) и точкой B({x2, y2} = {result}")
