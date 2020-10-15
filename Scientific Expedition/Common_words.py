# https://py.checkio.org/en/mission/common-words/

def checkio(line1: str, line2: str) -> str:
    line1_set = set(line1.split(','))
    line2_set = set(line2.split(','))

    return_str = ''
    for word in sorted(line1_set.intersection(line2_set)):
        return_str += word + ','
    return return_str[:-1]


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
