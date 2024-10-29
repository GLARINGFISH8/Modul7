def F():

    num1 = 0
    num2 = 1

    while True:
        yield num2
        num1, num2 = num2, num1 + num2
