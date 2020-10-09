# https://py.checkio.org/en/mission/sort-array-by-element-frequency/

def frequency_sort(items):
    items
    return_list = []
    for item in items:
        if item not in return_list:
            return_list += items.count(item) * [item]
    return sorted(return_list, key=lambda x: return_list.count(x), reverse=True)
    # return sorted(items, key=lambda x: items.count(x), reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
