def F(S, lenght=1):
    left_border = 0
    right_border = lenght

    while right_border <= len(S):
        yield S[left_border : right_border]

        left_border += 1
        right_border += 1
