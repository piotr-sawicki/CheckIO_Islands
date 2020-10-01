# https://py.checkio.org/en/mission/remove-all-before/

from typing import Iterable

class RemoverAllBefore:
    def __init__(self, items: list, border: int):
        self.items = items
        self.border = border

        try:
            self.index = self.items.index(border)
        except ValueError:
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.items[self.index]
            self.index += 1
            return result
        except IndexError:
            raise StopIteration

def remove_all_before(items: list, border: int) -> Iterable:
    return iter(RemoverAllBefore(items, border))


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
