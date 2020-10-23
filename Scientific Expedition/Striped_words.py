# https://py.checkio.org/mission/striped-words


import re

VOWELS = 'aeiouy'


def checkio(line: str) -> str:
    words = [word for word in re.split('[ ,.?!]', line) if word.isalpha() and len(word) > 1]
    i = 0
    for word in words:
        vowel = f'[{VOWELS}]'
        not_vowel = f'[^{VOWELS}]'

        vowel_pattern = ''
        not_vowel_pattern = ''
        for k in range(len(word)):
            if k % 2:
                vowel_pattern += vowel
                not_vowel_pattern += not_vowel
            else:
                vowel_pattern += not_vowel
                not_vowel_pattern += vowel

        pattern = f'{vowel_pattern}+|{not_vowel_pattern}+'
        if re.match(pattern, word.lower()):
            i += 1
    return i


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing

    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
