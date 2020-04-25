"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from sys import exit


def input_number() -> str:
    while True:
        try:
            num = input("Enter number: ")
            if int(num) <= 0:
                print('Your number is not simple')
                continue
        except ValueError:
            print("Wrong number")
            continue
        return num


def print_num(text_number: str, num: str, multiplicity: int, is_multiplicity: bool):
    print(f'{text_number}: ', end='')
    for dec in num:
        # Эта часть мне не нравится, но получше придумать не смог - код повторяется.
        if is_multiplicity:
            if int(dec) % multiplicity == 0:
                print(dec, sep='', end=' ')
        else:
            if int(dec) % multiplicity != 0:
                print(dec, sep='', end=' ')
    print()


def main():
    num = input_number()
    print_num('Even', num, 2, True)
    print_num('Odd', num, 2, False)


if __name__ == '__main__':
    main()
