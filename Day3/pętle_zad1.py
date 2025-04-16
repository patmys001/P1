# pętle - możliwośc wykonania kodu wielokrotnie
import random
from itertools import zip_longest

for i in range(5):
    print(i)

for i in range(5):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(10):
    print(i * 2)
    print(i + 2)
print(30 * "#")
print(30 * "#")
# przerobić lotto na wylosowanie 6 liczb za pomoca pętli

# lista_wynik = []
# lista_kul = list(range(1, 50))
# print(lista_kul)
# wynik = random.choice(lista_kul)
# lista_kul.remove(wynik)
# print(wynik)
# lista_wynik.append(wynik)
# print(lista_wynik)
#
# print(random.choices(lista_kul, k=6))

lista_wynik = []
lista_kul = list(range(1, 50))
for _ in range(6):
    wynik = random.choice(lista_kul)
    lista_kul.remove(wynik)
    lista_wynik.append(wynik)
print(lista_wynik)

# for i in range(10):
#     if i % 2 == 0:
#         print(i, "parzysta")
# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

for c in lista3:
    if c > 4:
        print("wieksze od")
    else:
        print("Mniejsze,  równe 4")

print(30 * "#")
print(30 * "#")
for i in range(0, 10, 2):
    print(i)
print(30 * "#")
print(30 * "#")
for i in range(-10, 0):
    print(i)
for i in range(10, 0, -1):
    print(i)
print(30 * "#")
print(30 * "#")

for c in lista3:
    if c == 2:
        c += 1
        print(c)
    print("rzy kazdym przejsciu pętli")

##############
print(30 * "#")
print(30 * "#")

imiona = ["Radek", "Tomek", "Zenek", "Ania"]

print(imiona)
print(type(imiona))

for imie in imiona:
    print(imie)

for i in range(len(imiona)):
    print(i, imiona[i])
print(30 * "#")
for p in imiona:
    print(imiona.index(p), p)
print(30 * "#")

# enumerae() - numeruje kolekcje i zwraca jej elementu i numer
for p in enumerate(imiona):
    print(p)
print(30 * "#")
for i, o in enumerate(imiona):
    print(i, o)
print(30 * "#")

for i, o in enumerate(imiona, start=1):
    print(i, o)
print(30 * "#")
print(30 * "#")
#################################
imiona = ["Radek", "Tomek", "Zenek", "Ania", "Roman"]
wiek = [44, 55, 32, 27]
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# zip() - łaczenie kolekcji
for i in zip(imiona, wiek):
    print(i)
for i, w in zip(imiona, wiek):
    print(i, w)
for i, (w, x) in enumerate(zip(imiona, wiek), start=1):
    print(i, w, x)
print(40 * "#")

###################################
imiona = ["Radek", "Tomek", "Zenek", "Ania", "Roman"]
wiek = [44, 55, 32, 27]
zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)
for i in zipped:
    print(i)

print(30 * "#")

for i, w in zipped:
    print(i, w)
zipped = zip_longest(imiona, wiek, fillvalue=None)
zipped_list = list(zipped)
for i, w in zipped_list:
    print(i, w)

