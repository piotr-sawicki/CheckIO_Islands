# https://py.checkio.org/en/mission/most-wanted-letter/

def checkio(text: str) -> str:
    letter_dict = {k: text.lower().count(k) for k in set(text.lower()) if ord(k) > 96 and ord(k) < 123}
    max_letters = []
    for k, v in letter_dict.items():

        if v == letter_dict[max(letter_dict, key=lambda i: letter_dict[i])]:
            max_letters.append(k)
    return sorted(max_letters)[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
