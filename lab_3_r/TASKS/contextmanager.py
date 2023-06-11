class ContextManager:
    def __enter__(self):
        print("Зашли в контекстный менеджер")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Нет ошибок")
        else:
            print(f"Произошла ошибка: {exc_type.__name__}:{exc_val}")
            return True

with ContextManager():

    print(1)
    print(1 / 0)