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
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import sys


def input_operands():
    num_a, num_b = None, None
    try:
        num_a = int(input("Enter first number: "))
        num_b = int(input("Enter second number: "))
    except ValueError:
        print("Wrong number")
        input_operands()
    return num_a, num_b


def insert_operator():
    operator = input("Enter operator sign: ")
    if operator == '0':
        print("Calc was shutdown.")
        sys.exit(0)
    if operator in operators_list:
        return operator
    print("Wrong operator")
    return insert_operator()


def main():
    num_a, num_b = input_operands()
    operator_sign = insert_operator()
    if operator_sign == '-':
        return num_a - num_b
    elif operator_sign == '+':
        return num_a + num_b
    elif operator_sign == '*':
        return num_a * num_b
    elif operator_sign == '/':
        if num_b == 0:
            return 'DivisionZeroError'
        return num_a / num_b
    else:
        return 'Some kind of shit is happened'


if __name__ == '__main__':
    operators_list = ['-', '+', '*', '/']
    while True:
        print(main())
