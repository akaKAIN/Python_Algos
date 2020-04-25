"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import randint


def sum_simple_numbers(limit):
    result = 0
    for i in range(limit+1):
        result += i
    return float(result)


def sum_by_expression(limit):
    return limit * (limit + 1) / 2


def main():
    number = randint(0, 10 ** 8)
    res_expr = sum_by_expression(number)
    res_simple = sum_simple_numbers(number)
    assert res_expr == res_simple, f"Something happened, and math laws was crash {res_expr} != {res_simple}"
    print("All's fine")


if __name__ == '__main__':
    main()
