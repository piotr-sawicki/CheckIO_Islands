# https://py.checkio.org/en/mission/bigger-price/

def find_max_price(data):
    flatten_data = [d['price'] for d in data]
    max_price = max(flatten_data)
    return flatten_data.index(max_price), max_price

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    result_list = []
    for i in range(limit):
        id_max_price, max_price = find_max_price(data)
        result_list.append(data.pop(id_max_price))
    return result_list


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
