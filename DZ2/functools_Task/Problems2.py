def Check_even(array: list[int]) -> list[int]:
    result = filter(lambda x: abs(x) % 2 == 0, array)

    return list(result)


