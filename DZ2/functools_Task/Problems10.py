from functools import reduce

def Search(array: list[int]) -> list[int]:
    result = reduce(lambda x, y: x * y,  filter(lambda x: x > 0, array))

    return result

