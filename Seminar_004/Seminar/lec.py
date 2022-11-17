"""
РЕКУРСИЯ 

"""

# for i in range(10, 0, -1):      # -1 это обратный отсчет
#     print(i)

# def count_down(n):              # - рекурсия (тоже самое)
#     print(n)
#     if n == 0:
#         return
#     count_down(n - 1)
# count_down(10)


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
print(factorial(5))