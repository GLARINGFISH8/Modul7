def param(*type_param):
    def type_check(func):
        def wrapper(*args, **kwargs):

            for index in range(0, len(args), 1):

                if not(isinstance(args[index], type_param[index])):
                    raise TypeError(f"Неверный тип аргумента '{func.__code__.co_varnames[index]}'. Ожидался {type_param[index]}, получен {type(args[index])}")

            result = func(*args, **kwargs)

            return result

        return wrapper

    return type_check



@param(int, int)
def greet(a, b):
    return a + b









