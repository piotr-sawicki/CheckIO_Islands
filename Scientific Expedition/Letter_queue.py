# https://py.checkio.org/en/mission/letter-queue/

from typing import List


class FIFO:
    def __init__(self):
        self.queue = []

    def pop(self):
        try:
            self.queue.pop(0)
        except IndexError:
            pass

    def push(self, item):
        self.queue.append(item)

    def get_letters(self):
        return_str = ''
        for letter in self.queue:
            return_str += letter
        return return_str

def letter_queue(commands: List[str]) -> str:
    queue = FIFO()
    for command in commands:
        if command == 'POP':
            queue.pop()
        else:
            _, letter = command.split()
            queue.push(letter)
    return queue.get_letters()


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
