from functools import reduce
import math

def F(arr:[int]) -> int:
    result = reduce(lambda x, y: x * y,   map(math.factorial, filter(lambda x: x % 2 == 0, arr)))

    return result

