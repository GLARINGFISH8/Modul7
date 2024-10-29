def F(N):
    acc = 1

    while True:
        if acc > N:
            break

        if acc % 3 != 0:
            yield acc

        acc += 1
