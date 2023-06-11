def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print("значение уже вычислялось")
            return cached_results[args]

        else:
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper

@cache
def my_func(n):
    return n**2


print(my_func(2))
print(my_func(5))
print(my_func(2))