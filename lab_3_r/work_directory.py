from Talayserializer.serialiser import serialize, deserialize
from Talayserializer import serializer_zavod

def my_func(a):
    return a+3

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner
#ser = serialize(my_func)

#deser = deserialize(ser)

#print(deser(2))

zavod = serializer_zavod.zavod.create_zavod('json')

zavod.dump(my_func, open('test_2.json', 'w'))

with open("test_2.json", "w") as fs:
    zavod.dump(my_func, fs)


