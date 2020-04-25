"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 45
Введите второе число: 56
Результат 45 + 56 = 101
Введите операцию (+, -, *, / или 0 для выхода): rth
Неверная операция. Повторите ввод
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import sys


class Calc:
    __slots__ = ['num_a', 'num_b', 'operator_map']

    def __init__(self):
        self.num_a: int
        self.num_b: int
        self.operator_map = {
            '0': self.stop,
            '-': self.my_sub,
            '+': self.my_add,
            '*': self.my_mul,
            '/': self.my_div
        }

    @staticmethod
    def stop():
        print("Calc was shutdown")
        sys.exit(0)

    def my_sub(self):
        return self.num_a - self.num_b

    def my_add(self):
        return self.num_a + self.num_b

    def my_mul(self):
        return self.num_a * self.num_b

    def my_div(self):
        if self.num_b == 0:
            return 'DivisionZeroError'
        return self.num_a / self.num_b

    def input_data(self):
        result = True
        num_a, num_b = None, None
        try:
            print('=====================================')
            num_a = int(input("Enter first number: "))
            num_b = int(input("Enter second number: "))
            print('=====================================')
        except ValueError:
            result = False
            print("Wrong number!")

        if result:
            self.num_a = num_a
            self.num_b = num_b
        return result

    def input_operator(self):
        operator = input("Enter operator sign (or 0 for exit): ")
        if operator in self.operator_map.keys():
            return self.operator_map[operator]
        print("Unknown operator")
        return self.input_operator()

    def main(self):
        while True:
            if self.input_data():
                print(self.input_operator()())


if __name__ == '__main__':
    Calc().main()

