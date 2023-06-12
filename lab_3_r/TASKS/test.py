class Meta(type):
    def __new__(cls, name, base, attrs):
        new_name = name.lower()
        return super().__new__(cls, new_name, base, attrs)

class BIGCLASS(metaclass=Meta):
    pass

a = BIGCLASS()
print(a.__class__.__name__)
