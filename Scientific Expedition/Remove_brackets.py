# https://py.checkio.org/mission/remove-brackets


def balanced(line: str) -> bool:
    tmp_line = line.replace('()', '').replace('[]', '').replace('{}', '')
    if line == '':
        return True
    elif tmp_line != line:
        return balanced(tmp_line)
    else:
        return False


def remove_brackets(line: str) -> str:
    if balanced(line):
        return line

    result = ''
    for i in range(len(line)):
        reduced_line = line[:i] + line[i+1:]
        smaller_result = remove_brackets(reduced_line)  # reduces line argument by one element (recursively)
        if len(smaller_result) > len(result): # returns the longest balanced result
            result = smaller_result
    return result


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
