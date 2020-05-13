"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


# Стандартный подход
def bubble_sort(ARR):
    w = 1

    while w < len(ARR):
        for i in range(len(ARR) - w):
            if ARR[i] < ARR[i + 1]:
                ARR[i], ARR[i + 1] = ARR[i + 1], ARR[i]
        w += 1
    return ARR


# Дорабртанный
# Если за проход не совершается ни одной сортировки то прекращение

def bubble_sort_upgrade(ARR):
    q = 1
    no_sort = 0

    while q < len(ARR):
        for i in range(len(ARR) - q):
            if ARR[i] < ARR[i + 1]:
                ARR[i], ARR[i + 1] = ARR[i + 1], ARR[i]
                no_sort = 1
        if no_sort == 0:
            break
        q += 1
    return ARR


if __name__ == '__main__':
    LIST = [random.randint(-100, 100) for i in range(10)]
    print(bubble_sort(LIST))
    print(bubble_sort_upgrade(LIST))

    print(timeit.timeit("bubble_sort(LIST)", setup="from __main__ import bubble_sort, LIST"))
    print(timeit.timeit("bubble_sort_upgrade(LIST)", setup="from __main__ import bubble_sort_upgrade, LIST"))
