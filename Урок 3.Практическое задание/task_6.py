"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
from random import randrange


def input_len_list():
    count = int(input("Введите количество элементов в массиве: "))
    arr = [randrange(100) for _ in range(count)]
    print(f"Массив: {arr}")
    return arr


def get_slice(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    a = arr[min_index:max_index+1]
    b = arr[max_index:min_index+1]
    return a if len(a) > 0 else b


def main():
    arr = input_len_list()
    s = get_slice(arr)
    min_num = s[0] if s[0] < s[-1] else s[-1]
    max_num = s[-1] if s[0] < s[-1] else s[0]
    print(f"Сумма элементов между минимальным {min_num}  и максимальным {max_num} элементами: {sum(s[1:-1])}")


if __name__ == '__main__':
    main()
