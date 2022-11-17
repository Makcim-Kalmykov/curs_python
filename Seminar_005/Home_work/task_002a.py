"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""

"""
import random


############# ВАРИАНТ a ##################

def open_filse ():
    pach = "task_002.txt"
    data = open(pach, "r", encoding="utf-8")
    for line in data:
        numb = line
    return int(numb)

def input_number_int_positive():                # ввод целого числа больше от 1 до 28
    num = ""
    temp = False
    while temp == False:
        while num.isnumeric() == False:
            try:
                num = int(input(f"Введите целое число от 1 до 28: "))
                break
            except ValueError:
                print("Неверный ввод")
                continue
        num = int(num)
        if (num == 0 or num < 0 or num > 28):
            print("Введеное число меньше или равно 0, либо больше 28")
            num = ""
        else:
            temp = True
    return num

def serch_winner(motion, current, name_player):
    names = name_player
    while current > 28:
        
        if motion % 2 != 0:
            player = 1
            motion = 1
        else:
            player = 2

        print(f"На столе осталось {current} конфет")
        
        if player == 1:
            print(f"{names}, введите кол-во конфет:")
            temp = input_number_int_positive()
        else:
            temp = random.randint(1, 28)
            print(f"Бот ввел число: {temp}")


        current = current - temp
        motion += 1
        print()

    if motion == 2:
            print(f"Осталось {current} конфет. Победил бот ")
    else:
            print(f"Осталось {current} конфет. {names}, вы победили")

name = str(input("Введите Ваше имя: "))
print()

numbers = open_filse()
num = random.randint(1, 2)
serch_winner(num, numbers, name)