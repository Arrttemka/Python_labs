def create_meta():
    class Meta(type):
        def __new__(cls, name, bases, attrs):
            int_attrs = {key: value for key, value in attrs.items() if isinstance(value, int)}
            return super().__new__(cls, name, bases, int_attrs)
    return Meta
MetaClass = create_meta()

class MyClass(metaclass=MetaClass):
    x = 10
    y = "ten"

print(MyClass.x)
# print(MyClass.y)

print(hasattr(MyClass, "x"))
print(hasattr(MyClass, "y"))