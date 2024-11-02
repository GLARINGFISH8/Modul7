# Task1.1
def F1(A, B):
    for i in range(A, B - 1, -1):
        yield i


# Task1.2

def F2():
    num1 = 0
    num2 = 1

    while True:
        if num2 % 5 == 0:
            yield num2

        num1, num2 = num2, num2 + num1



#Task1.3
def F3():

    k = 0
    while True:
        k += 1
        fact = 1

        for i in range(1, k + 1, 1):
            fact *= i

        yield fact


#Task1.4

def F4():
    unicode_num = 65

    while True:
        if unicode_num > 90:
            unicode_num = 65

        yield chr(unicode_num)
        unicode_num += 1

#Task1.5

def F5(string:str):
    string = string.replace('.', '').replace(',', '')
    arr = set(string.split())

    for elem in arr:
        yield elem



#Task1.6

def F6(string, K):
    string = string.replace('.', '').replace(',', '')
    arr = string.split()

    arr = filter(lambda x: len(x) > K, arr)
    arr = sorted(arr, key=len, reverse=True)

    for elem in arr:
        yield elem


#Task1.7
from itertools import permutations

def F7(string, N):
    for j in range(0, N, 1):
        characters = list(string)
        perm = permutations(characters, N)
        options = [''.join(p) for p in perm]

        for i in options:
            yield i

        N -= 1





#Task1.8

def F8(string):
    string = string.replace('.', '').replace(',', '')
    arr = string.split()

    Vowels = ['a', 'e', 'i', 'o', 'u']
    Unigue = []

    for elem in string:
        for j in elem:

            if (j in Vowels) and not(j in Unigue):
                Unigue.append(j)
                yield j





























