
# Zbiory
zbior1 = { 1, True, 0, False, 2, "ABC"}
print(zbior1)

lista1 = [ 1, True, 0, False, 2, "ABC"]
print(list(set(lista1)))

#print(zbior1[0])
for item in zbior1:
    print(item)

zbiorA = set()
for x in range(1, 11):
    zbiorA.add(x)

zbiorB = set()
for x in range(8, 16):
    zbiorB.add(x)

print(f"A={zbiorA}")
print(f"B={zbiorB}")
print("unia:", zbiorA.union(zbiorB))
print("część wsp.:", zbiorA.intersection(zbiorB))
print("różnica:", zbiorA.difference(zbiorB))
print("różnica symetryczna:", zbiorA.symmetric_difference(zbiorB))