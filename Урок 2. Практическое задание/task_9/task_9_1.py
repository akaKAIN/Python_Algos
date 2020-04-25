"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def decimal_sum(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result


def input_num(text):
    while True:
        try:
            num = int(input(text))
            return abs(num)
        except ValueError:
            print("Wrong number")


def main():
    max_sum, max_num = 0, 0
    count = input_num("Enter count of numbers: ")
    for i in range(count):
        temp_num = input_num("Enter number: ")
        temp_sum = decimal_sum(temp_num)
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_num = temp_num
    print(f"Max sum of decimal numbers in {max_num}, sum of decimals is {max_sum}")


if __name__ == '__main__':
    main()

