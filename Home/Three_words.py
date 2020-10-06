# https://py.checkio.org/en/mission/three-words/

import re


def checkio(words: str) -> bool:
    words_list = words.split(' ')
    k = 0
    for word in words_list:
        print(word, re.search(r'\d', word))
        if re.search(r'\d', word):
            k = 0
        else:
            k += 1

        if k == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
