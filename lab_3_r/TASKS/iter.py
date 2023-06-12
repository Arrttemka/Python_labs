class PowerMaster:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 1:
            rez = self.number ** 2
            self.number -= 1
            return rez
        else:
            raise StopIteration

pm = PowerMaster(5)
for ite in pm:
    print(ite)

# rm = PowerMaster(5)
# i = iter(rm)
# for it in rm:
#     print(next(i))