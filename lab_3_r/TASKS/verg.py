def cache(func):
    result: dict[tuple, object] = {}
    is_computed = False

    def wrapper(*args, **kwargs):
        nonlocal is_computed
        key = tuple(args, *kwargs.items())
        if key not in result:
            result[key] = func(*args, **kwargs)
            if not is_computed:
                print("Вычисление выполнено и сохранено в кэше.")
                is_computed = True
        else:
            print("Результат получен из кэша.")
        return result[key]

    return wrapper


@cache
def fib(n):
    if n < 2:
        return 1
    return n * fib(n - 1)


print(fib(300))
print(fib(300))
