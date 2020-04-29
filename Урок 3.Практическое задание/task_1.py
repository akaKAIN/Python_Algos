"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""


def create_dict():
    d = {}
    for i in range(2, 10):
        d.setdefault(str(i), 0)
    return d


def print_result(d: dict):
    for key, val in d.items():
        print(f"В диапазоне 2-99: {val} чисел кратны {key}")


def main():
    result_dict = create_dict()
    for i in range(2, 100):
        for j in range(2, 10):
            if i >= j and i % j == 0:
                result_dict[str(j)] += 1
    print_result(result_dict)


if __name__ == '__main__':
    main()
