def Transformation(array: list[str]) -> list[int]:
    result = map(lambda x: int(x) ** 2,  filter(lambda x: abs(int(x)) % 2 == 0, array))

    return list(result)

