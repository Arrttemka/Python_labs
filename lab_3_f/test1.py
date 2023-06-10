def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  # Создание ключа на основе аргументов и ключевых аргументов
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper


@memoize
def my_func(n):
    return n**2


print(my_func(2))
print(my_func(5))
print(my_func(2))