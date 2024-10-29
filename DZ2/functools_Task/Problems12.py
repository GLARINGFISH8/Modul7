def F(array: list[str]) -> list[str]:
    result = filter(lambda x: x == x[: : -1], array)

    return list(result)


