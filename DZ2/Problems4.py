def CheckLenStr(array: list[str]):
    result = filter(lambda x: len(x) > 3, array)

    return list(result)