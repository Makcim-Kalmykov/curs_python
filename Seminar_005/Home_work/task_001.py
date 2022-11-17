"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

"""

def delete_text(lst_text, find):
    temp = lst_text.split(" ")                     # разбиваем строку на список слов
    lst = []
    for i in temp:
        if find not in i:                           # ищем в списке слов необходимые символы
            lst.append(i)
    temp = ' '. join(lst)                           # склеиваем новый список в строку
    return temp


def open_filse ():
    pach = "task_001.txt"
    data = open(pach, "r", encoding="utf-8")
    for line in data:
        text = "" + line
    return text


text_new = open_filse()
find_text = "абв"
print(delete_text(text_new, find_text))