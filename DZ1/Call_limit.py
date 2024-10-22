def param(max_calls):
    def call_limit(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1

            if not(count < max_calls):
                raise RuntimeError("Превышено максимальное количество вызовов функци")

            result = func(*args, **kwargs)

            return result
        return wrapper
    return call_limit



