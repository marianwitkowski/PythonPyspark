# generator
from functools import lru_cache
import time

@lru_cache(128)
def fibo_rek(n):
    if n <= 1:
        return n
    else:
        return fibo_rek(n - 2) + fibo_rek(n - 1)

def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

ts1 = time.time()
print(fibo_rek(36))
ts2 = time.time()
print(ts2-ts1)

fib = fibo_gen()
for _ in range(7):
    print(next(fib))


# Dekorator
def mydecorator(fn):
    def inner_function():
        print("=== start ===")
        fn()
        print("=== koniec ===")
    return inner_function


@mydecorator
def hello_world():
    print("Hello world!")


hello_world()
