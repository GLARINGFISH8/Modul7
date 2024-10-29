from functools import reduce

def MaxLen(array: list[str]) -> list[str]:
    result = reduce(lambda x, y: x if len(x) > len(y) else y, array)

    return result