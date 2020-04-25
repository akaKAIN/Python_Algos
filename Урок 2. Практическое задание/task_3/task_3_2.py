"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def input_number():
    try:
        num = int(input("Enter number: "))
        return abs(num)
    except ValueError:
        print("Wrong number")
        input_number()


def print_reversed_num(num):
    if num < 10:
        print(num, end='', sep='')
        return
    dec = num % 10
    num //= 10
    print(dec, end='', sep='')
    print_reversed_num(num)


def main():
    num = input_number()
    print('Revers number is: ', end='', sep='')
    print_reversed_num(num)


if __name__ == '__main__':
    main()

