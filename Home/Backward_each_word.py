# https://py.checkio.org/en/mission/backward-each-word/

def backward_string_by_word(text: str) -> str:
    words = text.split()
    backward_words = ''
    return_text = ''

    for bw in [word[::-1] for word in words]:
        backward_words += bw

    i = 0
    for char_id in range(len(text)):
        if text[char_id] == ' ':
            return_text += ' '
        else:
            return_text += backward_words[i]
            i += 1
    return return_text


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
