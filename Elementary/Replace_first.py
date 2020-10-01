# https://py.checkio.org/en/mission/replace-first/

from typing import Iterable


class MyIterator:
    def __init__(self, items):
        self.items = items
        self.number_of_items = len(items)
        self.end = False

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        if self.end and self.index == 1:
            raise StopIteration

        result = self.items[self.index]

        self.index += 1
        if self.index == self.number_of_items:
            self.index = 0
            self.end = True

        return result


def replace_first(items: list) -> Iterable:
    if len(items) in [0, 1]:
        return items
    else:
        # return iter(MyIterator(items)) # this is just another solution
        return items[1:] + [items[0]]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
