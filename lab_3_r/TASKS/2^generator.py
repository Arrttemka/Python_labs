def power_of_two_generator():
    power = 0
    while True:
        yield 2 ** power
        power += 1

pow_two = power_of_two_generator()

# Генерируем первые 10 степеней двойки
for _ in range(10):
    print(next(pow_two))
