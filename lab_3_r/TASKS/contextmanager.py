class ContextManager:
    def __enter__(self):
        print("Зашли в контекстный менеджер")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Произошла ошибка: {exc_type.__name__}:{exc_val}")
            print("вышли из контекстного менеджера")
            return True

with ContextManager():

    print(1)
    print(1 / 0)