"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
import sys


try:
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    c = int(input("введите третье число: "))
except ValueError:
    print('Wrong numbers')
    sys.exit(1)

# if a <= b:
#     if a <= c <= b:
#         print("среднее число: ", c)
#     elif c >= b:
#         print("среднее число: ", b)
#     else:
#         print("среднее число: ", a)
# else:
#     if b <= c <= a:
#         print("среднее число: ", c)
#     elif c >= a:
#         print("среднее число: ", a)
#     else:
#         print("среднее число: ", b)

if b <= a <= c or b >= a >= c:
    print(f'middle_num is {a}')
elif a <= b <= c or a >= b >= c:
    print(f'middle_num is {b}')
elif a <= c <= b or a >= c >= b:
    print(f'middle_num is {c}')
else:
    print('something going wrong')
