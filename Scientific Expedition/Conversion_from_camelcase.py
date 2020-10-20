# https://py.checkio.org/en/mission/conversion-from-camelcase/


def from_camel_case(name):
    return_str = ''
    for letter_id, letter in enumerate(name):
        if letter.upper() == letter:
            if letter_id != 0:
                return_str += '_' + letter.lower()
            else:
                return_str += letter.lower()
        else:
            return_str += letter
    return return_str

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")