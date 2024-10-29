def F():
    acc = 1

    while True:
        yield acc ** 2
        acc += 1

