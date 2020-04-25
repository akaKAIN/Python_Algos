"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randrange


def guessing(secret_num: int, count: int):
    count += 1
    if count > 10:
        print(f'Number {secret_num} was made up')
        return
    try:
        user_num = int(input("Enter your number: "))
        if user_num > secret_num:
            print("Your number is greater")
            guessing(secret_num, count)
        elif user_num < secret_num:
            print("Your number is less")
            guessing(secret_num, count)
        else:
            print("You guessed!")
            return
    except ValueError:
        print("Wrong number")
        guessing(secret_num, count)


def main():
    secret_num = randrange(100)
    guessing(secret_num, 0)


if __name__ == '__main__':
    main()
