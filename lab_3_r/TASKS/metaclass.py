def create_int_metaclass():
    class IntMeta(type):
        def __new__(cls, name, bases, attrs):
            int_attrs = {key: value for key, value in attrs.items() if isinstance(value, int)}
            return super().__new__(cls, name, bases, int_attrs)

    return IntMeta
IntOnlyClass = create_int_metaclass()

class MyClass(metaclass=IntOnlyClass):
    x = 10
    y = "hello"
    z = 20

print(MyClass.x)  # Вывод: 10
print(MyClass.z)  # Вывод: 20
print(hasattr(MyClass, "x"))
print(hasattr(MyClass, "z"))
print(hasattr(MyClass, "y"))  # Вывод: False
