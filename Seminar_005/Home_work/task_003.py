"""
Создайте программу для игры в ""Крестики-нолики"".

"""
import random


def input_number(lst):
    num = ""
    temp = False
    
    while temp == False:
        while num.isnumeric() == False:
            try:
                num = int(input(f"Введите целое число от 1 до 9: "))
                break
            except ValueError:
                print("Неверный ввод")
                continue
        num = int(num)
        if (num == 0 or num < 0 or num > 9):
            print("Введеное число меньше или равно 0, либо больше 9")
            num = ""
        elif (str(num) != lst[num - 1]):
            print("Данная ячейка уже занята!")
            num = ""
        else:
            temp = True
    return num

def game_result(lst, player_1, player_2, move):
    global number
    count = 0
    winner = 0
    while count < 9:
        if move == 0:
            print(f"{player_1} поставьте Х в свободное поле (от 1 до 9). Укажите цифру ячейки: ")
            move = 1
            number = input_number(lst)
            lst[number - 1] = str('X')

        else:
            print(f"{player_2} поставьте O в свободное поле (от 1 до 9). Укажите цифру ячейки: ")
            move = 0
            number = input_number(lst)
            lst[number - 1] = str('O')

        print()
        print(f"{list[:3]}\n{list[3:6]}\n{list[6:]}")
        print()
        winner = check_finish(lst)
        
        if winner >= 1:
            break

    return winner       

def check_finish(lst):
    if  (lst[0] and lst[1] and lst[2]) == "X" or \
        (lst[3] and lst[4] and lst[5]) == "X" or \
        (lst[6] and lst[7] and lst[8]) == "X" or \
        (lst[0] and lst[3] and lst[6]) == "X" or \
        (lst[1] and lst[4] and lst[7]) == "X" or \
        (lst[2] and lst[5] and lst[8]) == "X" or \
        (lst[0] and lst[4] and lst[8]) == "X" or \
        (lst[2] and lst[4] and lst[6]) == "X":
        return 1

    elif (lst[0] and lst[1] and lst[2]) == "O" or \
         (lst[3] and lst[4] and lst[5]) == "O" or \
         (lst[6] and lst[7] and lst[8]) == "O" or \
         (lst[0] and lst[3] and lst[6]) == "O" or \
         (lst[1] and lst[4] and lst[7]) == "O" or \
         (lst[2] and lst[5] and lst[8]) == "O" or \
         (lst[0] and lst[4] and lst[8]) == "O" or \
         (lst[2] and lst[4] and lst[6]) == "O":
        return 2

    else:
        return 0
        

player1 = input("Игрок 1 - введите свое имя:")
player2 = input("Игрок 2 - введите свое имя:")

list = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']
print(f"{list[:3]}\n{list[3:6]}\n{list[6:]}")
print()

print("Право первого хода определится случайно.")
first_move = random.randint(0,1)

winner = game_result(list, player1, player2, first_move)

if winner == 0: 
    print("Победителя нет")
elif winner == 1:
    print(f"Победил игорок {player1}")
else:
    print(f"Победил игорок {player2}")



