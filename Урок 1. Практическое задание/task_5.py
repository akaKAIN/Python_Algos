"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""
a = input("введите первую букву: ")
b = input("введите вторую букву: ")

print("первая буква стоит на %d месте" % (ord(a) - ord('a') + 1))
print("вторая буква стоит на %d месте" % (ord(b) - ord('a') + 1))

num = abs(ord(a) - ord(b))

if num > 0:
    num -= 1

print("количество букв между введёнными: ", num)
