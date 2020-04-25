"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_func(num, count):
    if count == 1:
        return num
    old_num = num
    num /= -2
    count -= 1
    return old_num + recursion_func(num, count)


def input_number():
    try:
        return int(input("Enter number: "))
    except ValueError:
        input_number()


def main():
    num = input_number()
    result = recursion_func(1, num)
    print(result)


if __name__ == '__main__':
    main()
