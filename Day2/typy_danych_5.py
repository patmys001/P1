# Słownik-typ danych klucz wartość
# {'user':'Rade'}
# odpowiednik jasno
# klucze nie mogą się powtarzac
from logging.config import dictConfig

# pusty słownik
dictionary = {}
print(dictionary)
print(type(dictionary))

dictionary_1 = dict()
print(type(dictionary_1))
print(dictionary_1)
print("//----------------")
# dodanie do słownika
dictionary["imie"] = "Patryk"
print(dictionary)
dictionary["wiek"] = 67
print(dictionary)
print("//----------------")
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print("//----------------")
# nadpisanie elementu
dictionary["imie"] = "Tomek"
print(dictionary)
print(type(dictionary))
print("//----------------")
# wypisanie wartości
print(dictionary["imie"])
# print(dictionary["Imie"])
print(dictionary.get("Imie"))
print(dictionary.get("Imie", "default"))
dictionary.update({"data": "31-12-2025"})
print(dictionary)
dict_small = {"x", 2}
print(dict_small)
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)
print("//----------------")
print(15 * "/-/")

# input() - wprowadzanie danych do komputera z np. klawaitury
# tekst = input("Podaj imie")
# print(tekst)
# napisac aplikacje kalkulator
# pobrac liczby
# wyświetlić wynik działania np. dodawanie
# powitanie = "witaj w calc dodawanie"
# print(powitanie)
# a = int(input("Podaj A")) # bo zwykły input zwraca stringa
# b = int(input("Podaj B"))
# wynik= a+b
# print(a)
# print(b)
# print(wynik)
# print(type(wynik))
print(15 * "/-/")
# słownik polsko - angielski
# print("Słownik polsko-angielski")
# pol_ang = {"kot": "cat"}
# print(f'znam takie słowa: {pol_ang.keys()}')
# odp = input("Podaj słówko do przetłumaczenia")
# print(pol_ang[odp.strip().lower])
# print(pol_ang.get(odp.strip().lower(), "Nie mo"))
print(15 * "/-/")
name1 = "GROSS"
name2 = "groẞ"
print(name1.lower() == name2.lower())
print(name1.casefold() == name2.casefold())
print(15 * "/-/")

