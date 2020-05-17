"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter
from queue import Queue
import heapq


class Node:
    def __init__(self, value, code=''):
        self.value = value
        self.code = code
        self.code_dict = {}
        self.left_branch = None
        self.right_branch = None

    def __str__(self):
        return f'{self.__dict__}'

    def insert_value(self, value, code=''):
        if self.value > value:
            self.__insert_left(value, code + '0')
        elif self.value < value:
            self.__insert_right(value, code + '1')

    def __insert_left(self, value, code):
        if self.left_branch is None:
            self.left_branch = Node(value=value, code=code)
        elif self.left_branch is not None:
            self.left_branch.insert_value(value=value, code=code)

    def __insert_right(self, value, code):
        if self.right_branch is None:
            self.right_branch = Node(value=value, code=code)
        elif self.right_branch is not None:
            self.right_branch.insert_value(value=value, code=code)

    def bfs_node_step(self):
        result = [branch for branch in [self.right_branch, self.left_branch] if branch is not None]
        return result

    def walk(self):
        q = Queue()
        q.put(self)

        while not q.empty():
            node = q.get()
            self.code_dict.update({node.value: node.code})
            for branch in node.bfs_node_step():
                q.put(branch)


class Heap:
    def __init__(self, string):
        self.char_list = list(string)
        self.heap = self.make_heap_from_string()
        self.counts = Counter(self.heap)

    def make_heap_from_string(self):
        char_list = self.char_list[:]
        heapq.heapify(char_list)
        return char_list

    def __str__(self):
        return f'{self.__dict__}'

    def get_first_key(self):
        for key in self.counts.keys():
            return key


def show_result(tree, heap):
    for char in heap.char_list:
        print(tree.code_dict[char], end=' ', sep='')


def main():
    s = "AbracadaBra"
    h = Heap(s)
    print(h)
    seed, seed_code = (h.get_first_key(), '0')
    tree = Node(seed, seed_code)
    for key, val in h.counts.items():
        tree.insert_value(key)
    tree.walk()
    print(h.char_list)
    show_result(tree, h)


if __name__ == '__main__':
    main()


# Хм ... профита от реализации кучи в конце не увидел. только если брать с нее вершину.
# a = Node(5)
# a.insert_value(6)   # b - r
# a.insert_value(4)   # c - l
# a.insert_value(3)   # d - ll
# a.insert_value(7)   # e - rr
#
# b = a.right_branch
# c = a.left_branch
# d = c.left_branch
# e = b.right_branch
# print(f'{a.value=} {a.code=}\n{b.value=} {b.code=}\n{c.value=} {c.code=}\n')
# print(d, e)
# a.walk()
