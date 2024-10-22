
def uppercase_result(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if not(isinstance(result, str)):
            return result

        return result.upper()

    return wrapper


@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Александр"))
