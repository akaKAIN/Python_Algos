"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def input_number():
    while True:
        try:
            num = int(input("Enter number: "))
            return abs(num)
        except ValueError:
            print("Wrong number")


def main():
    num = input_number()
    print('Revers number is: ', end='', sep='')
    while num > 0:
        dec = num % 10
        num //= 10
        print(dec, end='', sep='')


if __name__ == '__main__':
    main()
