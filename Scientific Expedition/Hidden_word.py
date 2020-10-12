# https://py.checkio.org/en/mission/hidden-word/


def checkio(text, word):
    text = [text_line.replace(' ', '').lower() for text_line in text.split('\n')]
    for row_id, row in enumerate(text):
        try:
            col_start = row.index(word) + 1
            cold_end = col_start + len(word) - 1
            return [row_id + 1, col_start, row_id + 1, cold_end]
        except ValueError:
            pass
    for col_id in range(max([len(_) for _ in text])):
        column_str = ''
        for row in text:
            try:
                character = row[col_id]
            except IndexError:
                character = ''
            column_str += character
        try:
            row_start = column_str.index(word) + 1
            row_end = row_start + len(word) - 1
            return [row_start, col_id + 1, row_end, col_id + 1]
        except ValueError as error:
            pass


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
