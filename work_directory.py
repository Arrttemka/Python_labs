from Talay_serializer.serialiser import serialize, deserialize
from Talay_serializer import serializer_zavod

def my_func(a):
    return a+3

#ser = serialize(my_func)

#deser = deserialize(ser)

#print(deser(2))

zavod = serializer_zavod.zavod.create_zavod('json')

#zavod.dump(my_func, open('test_2.json', 'w'))

with open("test_2.json", "w") as fs:
    zavod.dump(my_func, fs)

with open("test_2.json", "r") as fs:
    des = zavod.load(fs)
