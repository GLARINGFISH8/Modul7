from functools import reduce

def F(array:list[str]) -> str:
    result = reduce(lambda x, y: f"{x} {y}",  map(lambda x: x.upper(), filter(lambda x: len(x) % 2 == 0, array)))

    return result

