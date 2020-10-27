# https://py.checkio.org/en/mission/yaml-more-types/

def translate(v):
    replace_dict = {
        'null': None,
        '': None,
        'true': True,
        'True': True,
        'false': False,
        'False': False
    }
    try:
        value = int(v)
    except ValueError:
        if v in replace_dict:
            value = replace_dict[v]
        elif v.startswith('"') and v.endswith('"'):
            value = v[1:-1].replace('\\', '')
        else:
            value = v
    return value


def yaml(a):
    return_dict = {k: translate(v) for k, _, v
                   in (map(str.strip, line.partition(':'))
                       for line in a.splitlines())
                   if k != ''}
    return return_dict

if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
