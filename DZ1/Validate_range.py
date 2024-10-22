def param(min_value, max_value):
    def validate_range(func):
        def wrapper(*args, **kwargs):

            for index in range(0, len(args), 1):

                if not(isinstance(args[index], (float, int))):
                    raise TypeError(f"Неверный тип аргумента '{func.__code__.co_varnames[index]}'. Ожидался {int} или {float}, получен {type(args[index])}")


                if not( (min_value < args[index]) or (max_value > args[index]) ):
                    raise TypeError(f"Аргумент '{func.__code__.co_varnames[index]}' имеет значение {args[index]}, что выходит за пределы {[min_value, max_value]}")


            result = func(*args, **kwargs)

            return result

        return wrapper

    return validate_range



@param(min_value=0, max_value=100)
def set_percentage(value, tara):
    print(f"Установлено значение: {value}%")


