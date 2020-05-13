"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random


def merge_and_sort(LIST):
    if len(LIST) > 1:
        cen = len(LIST) // 2
        left = LIST[:cen]
        rigth = LIST[cen:]

        merge_and_sort(left)
        merge_and_sort(rigth)

        q = 0
        w = 0
        e = 0

        while q < len(left) and w < len(rigth):
            if left[q] < rigth[w]:
                LIST[e] = left[q]
                q += 1
            else:
                LIST[e] = rigth[w]
                w += 1
            e += 1

        while q < len(left):
            LIST[e] = left[q]
            q += 1
            e += 1

        while w < len(rigth):
            LIST[e] = rigth[w]
            w += 1
            e += 1


if __name__ == '__main__':
    NUMBER = int(input("Введите число элементов: "))
    LIST = [random.random() * 50 for i in range(NUMBER)]

    print(LIST)
    merge_and_sort(LIST)
    print(LIST)
