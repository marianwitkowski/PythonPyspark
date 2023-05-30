
# Map / Filter / Reduce

from functools import reduce

lista = [5, -2, 8, 10, 8, 9]

# mapowanie / funkcja map()

def kwadrat(x):
    return x** 2

print(list(map(kwadrat, lista)))
print(list(map(lambda z:z**2, lista)))

# deklaracja funkcji anonimowej
f1 = lambda a,b,c : (a+b)//c
print(f1(5.5,5,2))

# filtrowanie
print(list(filter(lambda x:x>5, lista)))

print(sum(lista))
print(reduce(lambda x,y:x+y, lista))

# silnia
print(reduce(lambda x,y:x*y, [1,2,3,4,5]))


