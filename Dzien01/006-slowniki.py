
# Słowniki
osoba = dict()
osoba = {
    "imie": "Jan", "nazwisko": "Kowalski",
    "wiek": 44, "dostep": [101, 102, 103]
}
print(osoba)
print(osoba["imie"])
print(osoba.get("imie"), osoba.get("imiE","BRAK"))

# aktualizacja słownika
osoba["imie"] = "Andrzej"
osoba["imie2"] = "Paweł"
osoba.update({
    "imie2" : "Maria", "pesel": "1234567890"
})
print(osoba)
osoba.pop("pesel") # usuwanie klucza
del(osoba["imie2"]) # usuwanie klucza
print(osoba)

print("klucze:", osoba.keys())
print("wartosci:", osoba.values())
print("klucz/wartosc:", osoba.items())

iso_code = ["PL", "DE", "GB", "FR"]
countries = ["Polska", "Niemcy", "Wlk Bryt.", "Francja"]

ix = iso_code.index("DE")
print(countries[ix])

countries_codes = {
    "PL" : "Polska", "DE" : "Niemcy", "FR" : "Francja"
}
print(countries_codes.get("DE"))

# sprawdzanie klucza w słowniku
if "PL" in countries_codes:
    print("Klucz PL istnieje")


