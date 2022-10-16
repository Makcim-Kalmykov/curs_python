"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

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
    



x = ImputNumber('x')
y = ImputNumber('y')
chetvert = 0
if x > 0 and y > 0:
    print(f"Точка с координатами ({x}, {y}) находится в {chetvert + 1} координатной четверти")
elif x < 0 and y > 0:
    print(f"Точка с координатами ({x}, {y}) находится в {chetvert + 2} координатной четверти")
elif x < 0 and y < 0:
        print(f"Точка с координатами ({x}, {y}) находится в {chetvert + 3} координатной четверти")
else:
    print(f"Точка с координатами ({x}, {y}) находится в {chetvert + 4} координатной четверти")
