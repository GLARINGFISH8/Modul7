from functools import reduce

def Mult_num(array: list[int]) -> list[int]:
    result = reduce(lambda x, y: x * y, array)

    return result


