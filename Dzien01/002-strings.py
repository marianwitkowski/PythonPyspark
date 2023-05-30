

# Łańcuchy znaków - string
s = ' Ala ma kota " \r\n Kolejna \t linia '
print(s)

s = r' Ala ma kota " \r\n Kolejna \t linia '
print(s)

s = "Bardzo długi string "*10

s = """
Linia 1
Linia 2
Linia 3
.....
"""

file_name = "C:\\tmp\\plik.txt"
file_name = r"C:\tmp\plik.txt"
file_name = "C:/tmp/plik.txt"

print(s.strip())
print(s.lower(), s.upper())
print(s.replace("old","new"))
print(s.count("A"))
print(s.index("la"))

if 3 in [10,40,3]:
    print("jest 3")

if "Ala" in s:
    print("Ala jest w stringu")

