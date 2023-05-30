
# Pętle w Pythonie

# a = 5; b = 10
a , b = 5, 10
print(a ,b)
tuple1 = (10, 20)
# x = tuple1[0]
# y = tuple1[1]
x, y = tuple1
tuple1 = (-10, -20)
print(x, y, len(tuple1))
tuple2 = (4,)

i = 10
while i> 0:
    print(i)
    i -= 1  # i = i - 1
    if i == 5: break

# Pętla for
result = []
for x in range(1, 21, 2):
    if x == 5:
        continue
    result.append(x ** 2)
print(result)

print("=" * 50)
lista = ['A', 1, None, (1, 'OK')]
for item in lista:
    print(item)

# symulacja ternary operator w Python
x = 10
result = None
if x > 10:
    result = "A"
else:
    result = "B"

result = "A" if x > 10 else "B"
result = ("B", "A")[x > 10]

print("=" * 50)
counter = 1
lista = ['A', 1, None, (1, 'OK')]
for item in lista:
    print(counter, item)
    counter += 1

print("=" * 50)
for counter, item in enumerate(lista, 100):
    print(counter, item)
