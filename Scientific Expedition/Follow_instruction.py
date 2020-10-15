# https://py.checkio.org/mission/follow-instructions

def follow(instructions):
    X, Y = 0, 0
    map_dict = {
        'f': 1,
        'b': -1,
        'r': 1,
        'l': -1
    }
    for i in instructions:
        if i in ['f', 'b']:
            Y += map_dict[i]
        else:
            X += map_dict[i]
    return X, Y


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
