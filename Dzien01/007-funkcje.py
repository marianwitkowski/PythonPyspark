
# Funkcje
import math

def foo():
    pass

def oblicz_pole_kola(r: float) -> float:
    if type(r) is int or type(r) is float:
        return math.pi*(r**2)
    else:
        return 0

def oblicz_obwod_kola(r):
    return 2*math.pi*r

def oblicz_kolo(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

pole, obwod = oblicz_kolo(2.5)
print(f"pole={pole:.3f}, obwod={obwod:.3f}")

# funkcja z paramtrami domyślnymi
def nowy_pracownik(imie, nazwisko,
                   telefon="611234567", email="biuro@firma.pl"):
    osoba = {
        "imie": imie, "nazwisko": nazwisko, "telefon": telefon, "email":email
    }
    return osoba

print(nowy_pracownik("Jan","Kowalski"))
print(nowy_pracownik("Jan","Kowalski", telefon="606111222"))
print(nowy_pracownik("Jan","Kowalski", "606111222"))
print(nowy_pracownik("Jan","Kowalski", email="jk@firma.pl"))
print(nowy_pracownik("Jan","Kowalski", "606111222", "jk@firma.pl"))
print(nowy_pracownik("Jan","Kowalski", email="jk@firma.pl", telefon="606111222"))

def wiele_parametrow(imie, nazwisko, *args):
    for arg in args:
        print(arg, type(arg))

print("="*50)
s = "="*50
print(len(s))
wiele_parametrow("Jan","Kowalski", "606111222", "jk@firma.pl")


def funkcja_params(arg1, arg2="---", **kwargs):
    print("imie=",kwargs.get("imie"))
    print("wiek=",kwargs.get("wiek"))
    print("zawod=",kwargs.get("zawod"))

funkcja_params("A", imie="Jan", wiek=44, zawod="stolarz", pesel="1234567890")