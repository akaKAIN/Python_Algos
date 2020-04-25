"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def input_number():
    while True:
        try:
            return int(input("Enter number: "))
        except ValueError:
            continue


def main():
    count = input_number()
    result = 0
    operand = 1
    while count != 0:
        count -= 1
        result += operand
        operand /= -2
    print(result)


if __name__ == '__main__':
    main()
