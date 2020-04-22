"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""

import sys

# first option
while True:
    try:
        SUM, MUL = 0, 1
        NUM = input("Enter you number:\n-> ")
        for unit in NUM:
            try:
                SUM += int(unit)
                MUL *= int(unit)
            except ValueError:
                print("Bad number, try again")
                continue
        print(f'sum={SUM}\tmul={MUL}')
        break
    except KeyboardInterrupt:
        print("Ok, good bye.")
        break

# second option
NUM, SUM, MUL = 0, 0, 1
try:
    NUM = int(input("Enter your number:\n-> "))
except ValueError as e:
    print(f'Wrong number: {e}')
    sys.exit(1)
if NUM < 100 or NUM > 1000:
    print("Your number is too big or small")
    sys.exit(1)

if NUM > 0:
    unit = NUM % 10
    NUM //= 10
    SUM += unit
    MUL *= unit
else:
    print(f'sum={SUM}\tmul={MUL}')
    sys.exit(0)

if NUM > 0:
    unit = NUM % 10
    NUM //= 10
    SUM += unit
    MUL *= unit
else:
    print(f'sum={SUM}\tmul={MUL}')
    sys.exit(0)

if NUM > 0:
    unit = NUM % 10
    NUM //= 10
    SUM += unit
    MUL *= unit
else:
    print(f'sum={SUM}\tmul={MUL}')
    sys.exit(0)

print(f'sum={SUM}\tmul={MUL}')





