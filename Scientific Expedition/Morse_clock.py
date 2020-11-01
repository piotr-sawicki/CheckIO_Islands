# https://py.checkio.org/en/mission/morse-clock/


def convert_to_morse(time: str) -> str:
    return '{:04b}'.format(int(time)).replace('0', '.').replace('1', '-')


def checkio(time_string: str) -> str:
    return ' : '.join(
        [' '.join(map(convert_to_morse, f'{int(time):02d}'))[1:]
         for time in time_string.split(':')])[1:]


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))
    print(checkio("00:1:02"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
