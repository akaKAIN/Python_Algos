"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random


def search(array):
    left = []
    right = []

    for i in range(len(array)):
        for k in range(len(array)):
            if array[i] > array[k]:
                left.append(array[k])
            if array[i] < array[k]:
                right.append(array[k])
            if array[i] == array[k] and i > k:
                left.append(array[k])
            if array[i] == array[k] and i < k:
                right.append(array[k])

        if len(left) == len(right):
            print(f'Медиана - {array[i]}')
            break
        left.clear()
        right.clear()


def main(num):
    array = [random.randint(0, 100) for i in range(2 * num + 1)]
    print("Массив - {}".format(array))
    search(array)


if __name__ == '__main__':
    m = int(input("Введите число, которое сгенерирует массив: "))
    main(m)
