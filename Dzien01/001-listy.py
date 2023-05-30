# komentarz

lista = -1.234
lista = [1, 2, "Ala ma kota", False, None, ['A', 'B', 'C']]
print(lista, len(lista), sep=" || ")
lista.append("koniec")
lista.append([1,2,3]) # [1,2,3]
print(lista)
lista.extend([1,2,3]) # [1,2,3]
print(lista)

lista.insert(1, "element drugi")
lista.remove(1) # usuniecie wartosci
first_item = lista.pop(0) # usuniecie spod indeksu 0
PI = 3.14159
lista.index("koniec") # pobranie informacji na temat pozycji elementu
lista_wartosci = [50, 10, -10]
lista_wartosci.sort(reverse=False) # sortowanie listy
lista2 = lista.copy()
lista2[1] = "XYZ"
print(lista)
print(lista2)

# list slicing
#        0 1 2 3  4  5  6   7   8
#                       -3, -2, -1
lista = [1,2,5,10,20,50,100,200,500]
# RULE - 3xS (start : stop : step)
print(lista[1:3]) # [2,5]  mat. <1,3)
print(lista[3:]) # [10,20,50,100,200,500]
print(lista[:4]) # [1,2,5,10]
print(lista[1:8:2]) # [2,10,50,200]
print(lista[-2:]) # [200,500]

# palindrom - sprawdzenie
s = "Kobyła ma mały bok"
s_oryg = s
s = s.lower().replace(" ","")
if s == s[::-1]:
    print(f"wyrażenie '{s_oryg}' jest palindromem")
else:
    print(f"wyrażenie '{s_oryg}' nie jest palindromem")






