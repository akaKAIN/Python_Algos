"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
ARR = [1, 2, 3, 4, 5, 6, 7, 8, 4]


def main(arr):
    return max(arr, key=arr.count)


if __name__ == '__main__':
    print(max(ARR, key=ARR.count))
