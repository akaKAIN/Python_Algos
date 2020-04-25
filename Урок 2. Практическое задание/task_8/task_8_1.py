"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def input_number(text):
    while True:
        try:
            num = input(text)
            return abs(int(num))
        except ValueError:
            print("Wrong number")


def consider_decimal(num, dec):
    # Извиняюсь, но прям скучно делать почти 20 заданий, через одно и тоже
    # пусть в этот раз будут словари? :)
    sd = {}
    for n in str(num):
        sd.setdefault(n, 0)
        sd[n] += 1
    return sd.get(str(dec), 0)


def main():
    dec_counter = 0
    count = input_number("Enter count of numbers: ")
    search_number = input_number("What number we will consider: ")
    for i in range(count):
        num = input_number("Enter number: ")
        dec_counter += consider_decimal(num, search_number)
    print(f'Count: {dec_counter}')


if __name__ == '__main__':
    main()
