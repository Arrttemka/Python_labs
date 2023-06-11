def limit(n):
    def wrapper(func):
        def inner(*args, **kwargs):
            if len(args) + len(kwargs) > n:
                raise ValueError("too much arguments")
            return func(*args, **kwargs)
        return inner
    return wrapper


@limit(3)
def sum_func(*args):
    return sum(args)

print(sum_func(1, 2, 3, 4))

