import time
#from time import time # import metody time z modułu time

# Wyrażenia listotwórcze
result = [x ** 2 for x in range(1,21) if 5 <= x <= 15]
print(result)

LOOP = 10_000

ts1 = time.time()
result = []
for _ in range(LOOP):
    for x in range(1, 1001):
        if x%3==0:
            result.append(x**2)
ts2 = time.time()
print(ts2-ts1)

ts1 = time.time()
for _ in range(LOOP):
    [x**2 for x in range(1, 1001) if x%3==0]
ts2 = time.time()
print(ts2-ts1)
