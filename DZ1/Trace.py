def trace(func):
    Count = 0

    def wrapper(*args, **kwargs):
        nonlocal Count
        Count += 1

        tab = "\t" * Count

        print(f"{tab} --> Вход в функцию {func.__name__} c аргументами {args}")
        Count += 1

        result = func(*args, **kwargs)

        print(f"{tab} <-- Выход из функции {func.__name__} с результатами {result}")
        Count -= 1

        return result
    return wrapper


@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial(3)



