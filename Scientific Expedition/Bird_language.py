# https://py.checkio.org/en/mission/bird-language/


VOWELS = "aeiouy"


def translate(phrase):
    result_str = ''
    for word in phrase.split():
        ignore_char = []
        for char_id, char in enumerate(word):
            if char_id not in ignore_char:
                ignore_char.append(char_id + 1)
                result_str += char
                if char in VOWELS:
                    ignore_char.append(char_id + 2)

        result_str += ' '
    return result_str[:-1]


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
