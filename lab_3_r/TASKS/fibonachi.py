def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

# Генерируем первые 10 чисел Фибоначчи
for _ in range(10):
    print(next(fib))
