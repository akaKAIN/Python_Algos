"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randrange


def generate_matrix():
    count_elem = int(input("Enter count of elements in row: "))
    count_row = int(input("Enter count of row in matrix: "))
    matrix = []
    for row in range(count_row):
        temp_row = [randrange(100) for _ in range(count_elem)]
        matrix.append(temp_row)
    return matrix


def get_min_column_elem(matrix: list):
    min_list = []
    count = len(matrix[0])
    for i in range(count):
        column = []
        for row in matrix:
            column.append(row[i])
        min_list.append(min(column))
    print(min_list, " min values in columns")
    print(f'Max of them is {max(min_list)}')


def main():
    matrix = generate_matrix()
    for i in matrix:
        print(i)
    get_min_column_elem(matrix)


if __name__ == '__main__':
    main()
