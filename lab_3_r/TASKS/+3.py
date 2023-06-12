def plus_three(func):
    def wrapper(args):
        if isinstance(args, int):
            return func(args**2)
        else:
            return func(args)
    return wrapper

@plus_three
def my_func(args):
    return args

print(my_func(3))

print(my_func("str"))
