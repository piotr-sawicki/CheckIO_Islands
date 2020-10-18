# https://py.checkio.org/mission/yaml-simple-dict


def yaml(a):
    return_dict = {}
    for line in a.split('\n'):
        try:
            key, value = line.split(': ')
            try:
                value = int(value)
            except ValueError:
                pass
            return_dict[key] = value
        except ValueError:
            pass
    return return_dict


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
