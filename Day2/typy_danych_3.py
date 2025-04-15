# krotka, tupla - niemutowalna lista
# pozwala efektywnie zarządzac pamięcią,
# może symulowac stale

tupla_imiona = ("Radek", "Tomek", "Zenek", "Mateusz")
print(tupla_imiona)
print(type(tupla_imiona))

print("//----------------")

tupla_liczby = 43, 55, 22, 34, 11, 200
print(tupla_liczby)
print(type(tupla_liczby))

print("//----------------")
tupla = 43
print(type(tupla))
tupla1 = (43)
print(type(tupla1))
tupla2 = 43,
print(type(tupla2))
tupla3 = (43,)
print(type(tupla3))
# tupla jest niemutowalna i nie można jej zmienić
print("//----------------")
del tupla_liczby

print("//----------------")
print(tupla_imiona.index("Radek"))
print(tupla_imiona.count("Radek"))

print("//----------------")
# rozpakowanie tup[li
tup = 1, 2
print(tup)
print(type(tup))
a, b = 1, 2
print(a, b)

a, b = tup
print(a, b)

tup2 = 1, 2, 3
# a, b = tup2
a, *b = tup2
print(a, b)
print("//----------------")
print(tupla_imiona)
name1, name2, *name3 = tupla_imiona  # * - oznacza pozostałe złap tutaj
# name1, *name2, name3 = tupla_imiona
print(tupla_imiona)
print(name1, name2, name3)

print("//----------------")
# sortowanie tupli zwraca listę
print(sorted(tupla_imiona))
print(type(sorted(tupla_imiona)))
print(tupla_imiona)
print("//----------------")

