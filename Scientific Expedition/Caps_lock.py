# https://py.checkio.org/en/mission/caps-lock/

def caps_lock(text: str) -> str:
    capslock = False
    return_str = ''
    for i in text:
        if i == 'a':
            capslock = ~capslock
        else:
            if capslock:
                return_str += i.upper()
            else:
                return_str += i

    return return_str


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
