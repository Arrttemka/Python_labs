class IntMeta(type):
    def __new__(cls, name, bases, attrs):
        int_attrs = {key : value for key, value in attrs.items() if isinstance(value, int)}
        return super().__new__(cls, name, bases, int_attrs)

class MyClass(metaclass=IntMeta):
    x = 10
    y = "str"

print(hasattr(MyClass, "x"))
print(hasattr(MyClass, "y"))