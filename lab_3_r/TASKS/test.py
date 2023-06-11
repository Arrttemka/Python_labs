class CountInstancesMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['instances_count'] = 0

        def __init__(self, *args, **kwargs):
            type(self).instances_count += 1
            super(self.__class__, self).__init__(*args, **kwargs)

        attrs['__init__'] = __init__
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=CountInstancesMeta):

    def sum(self, arg1, arg2):
        print(arg1 + arg2)

x = 10
y = 5
print(MyClass.instances_count)
a = MyClass()
a.sum(x, y)
print(MyClass.instances_count)