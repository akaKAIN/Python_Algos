"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
RAND_LIST = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]


def find_min_or_max(num):
    min_num, max_num = 10**8, -10**8
    for i in range(len(num)):
        if num[i] < min_num:
            min_num = num[i]
        if num[i] > max_num:
            max_num = num[i]
    return min_num, max_num


def main():
    min_num, max_num = find_min_or_max(RAND_LIST)
    for i in range(len(RAND_LIST)):
        if RAND_LIST[i] == min_num:
            RAND_LIST[i] = max_num
        elif RAND_LIST[i] == max_num:
            RAND_LIST[i] = min_num
    print(RAND_LIST)


if __name__ == '__main__':
    main()
