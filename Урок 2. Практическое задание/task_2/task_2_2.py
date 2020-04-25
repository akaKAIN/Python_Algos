"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from sys import exit


def input_number():
    try:
        num = int(input("Enter number: "))
        if num <= 0:
            return input_number()
    except ValueError:
        print("Wrong number")
        return input_number()
    return num


def math_operation_even(num):
    global even_row
    if num < 10:
        even_row += str(num)
        return num
    unit = num % 10
    if unit % 2 == 0:
        even_row += str(unit)
    num //= 10
    return math_operation_even(num)


def math_operation_odd(num):
    global odd_row
    if num < 10:
        odd_row += str(num)
        return num
    unit = num % 10
    if unit % 2 != 0:
        odd_row += str(unit)
    num //= 10
    return math_operation_odd(num)


def main():
    num = input_number()
    math_operation_even(num)
    math_operation_odd(num)


if __name__ == '__main__':
    even_row = ''
    odd_row = ''
    main()
    even_row = reversed(even_row)
    odd_row = reversed(odd_row)

    print('Even: ', sep='', end='')
    for i in even_row:
        print(i, end=' ')

    print()
    print('Odd: ', sep='', end='')
    for i in odd_row:
        print(i, end=' ')


