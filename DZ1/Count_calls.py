# №1

import time
def count_calls(func):
    Count = 0

    def wrapper(*args, **kwargs):
        nonlocal Count

        Count += 1

        print(f"Функция 'greet' вызвана {Count} раз(а)")

        func(*args, **kwargs)

    return wrapper


@count_calls
def greet(name: str) -> None:
    print(f"Привет, {name}!")

