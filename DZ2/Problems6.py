def ToConvertLen(array: list[str]) -> list[int]:
    result = map(lambda x: len(x), array)

    return list(result)