def F(A, B):
    acc = A

    while A <= acc < B:
        yield acc * 2
        acc += 1


