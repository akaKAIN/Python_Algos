"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
import sys


def input_matrix():
    matrix = []
    try:
        for elem_matrix in range(5):
            sum_input = 0
            row_input = []
            print(f'{elem_matrix + 1} row:')
            for i in range(4):
                num = int(input("Enter element of list: "))
                row_input.append(num)
                sum_input += num
            row_input.append(sum(row_input))
            matrix.append(row_input)
        print_matrix(matrix)
    except ValueError:
        print("Wrong number.")
        sys.exit(1)


def print_matrix(matrix: list):
    for row in matrix:
        print(row)


def main():
    input_matrix()


if __name__ == '__main__':
    main()
