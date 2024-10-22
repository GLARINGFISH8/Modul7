def F(array: list[str]) -> list[int]:

    result = map(lambda x: len(x),   filter(lambda s: s[0] in ["a", "e", "i", "o", "u", "y"], array))
    return list(result)

