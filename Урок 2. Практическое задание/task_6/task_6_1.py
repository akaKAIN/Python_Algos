"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random
from sys import exit


def input_user_number():
    while True:
        try:
            return int(input("Enter number: "))
        except ValueError:
            continue


def check_number(user_num, secret_num):
    if user_num > secret_num:
        return False, 'Your number is greater'
    elif user_num < secret_num:
        return False, 'Your number is less'
    else:
        return True, 'You guessed!'


def main():
    num = random.randrange(100)
    count = 10
    while count > 0:
        user_num = input_user_number()
        is_guessed, msg = check_number(user_num, num)
        print(msg)
        if is_guessed:
            exit(0)
        count -= 1
    print(f'Number {num} was made up')


if __name__ == '__main__':
    main()
