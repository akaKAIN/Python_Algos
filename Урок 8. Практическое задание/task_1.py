"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""
import copy
from hashlib import sha3_256 as sh


def get_smart_str(word, position):
    """Получение подстрок 'вправо' и 'влево' от указанной позиции, с привязанной границей (к позиции)"""
    result = []
    left_step = len(word[:position])
    right_step = len(word[position:-1])
    while left_step >= 0 and right_step < len(word) + 1:
        if left_step >= 0:
            result.append(word[left_step:position + 1])
            left_step -= 1
        if right_step < len(word) + 1:
            result.append(word[position:right_step + 1])
            right_step += 1
    return result


def generate_list(word):
    """Получение списка всех подстрок"""
    result = []
    for i in range(len(word)):
        result.extend(get_smart_str(word, i))
    result = list(set(result))
    for elem in ['', word]:
        result.remove(elem)
    return result


def print_substring_info(word):
    """Вывод отсортированного списка подстрок и поличества елементов в нем. Только для сравнения."""
    substrs = generate_list(word)
    substrs.sort(key=lambda x: len(x))
    print(f'{len(substrs)=}\n{substrs=}')


def hashed(phrase: str):
    """Функция возвращает хэш переданной строки"""
    return sh(phrase.encode()).hexdigest()


def get_count_substring(word_in):
    """Функция получения количества подстрок на основе сравнения хэшей"""
    hash_list = []
    simple_list = []
    count = 0
    full_hash_word = hashed(word_in)
    for i in range(len(word_in)):
        for le in range(len(word_in[:i + 1])):
            temp_hash = hashed(word_in[le:i + 1])
            if temp_hash not in hash_list and temp_hash != full_hash_word:
                hash_list.append(temp_hash)
                simple_list.append(word_in[le:i + 1])
                count += 1
        for ri in range(len(word_in[i:-1])):
            temp_hash = hashed(word_in[ri:])
            if temp_hash not in hash_list and temp_hash != full_hash_word:
                hash_list.append(temp_hash)
                simple_list.append(word_in[ri:])
                count += 1
    print(f'Итог: {count} подстрок')


def main():
    word = input('Enter your string: ')
    print_substring_info(word)
    get_count_substring(word)


if __name__ == '__main__':
    main()
