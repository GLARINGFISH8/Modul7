def F() -> list[int]:
    acc = 1

    while True:
        if acc % 5 == 0:
            yield acc

        acc += 1


