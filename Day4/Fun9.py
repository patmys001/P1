# funkcja lambda
# skrócona forma funkcji
# domyślnie ma return na końcu


def odejmij(a, b):
    return a - b


print(odejmij(7, 98))

odejmij2 = lambda a, b: a - b
print(odejmij2(3, 4))

# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100
vat2 = lambda k, v: k * v
print(vat2(100, 1.23))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 10 else "dorosły")
print(wiek(9))
print(wiek(21))
print(wiek(18))
print(wiek(17))
# mapowanie
lista = [1, 2, 3, 4, 24, 58, 100, 500]
lista_wynik = []
for i in lista:
    lista_wynik.append(i * 2)
    print(lista_wynik)
print([i * 2 for i in lista])


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)
# f wyższego rzedu map()- bierze lelementy kolejne i wykonuje na nich funkcje

print(f"zastosowanie funkcji map(){list(map(zmien, lista))}")

# funkcja anonimowa - prawdziwe zastosowanie anonimowe
print(f"zastosowanie funkcji map(){list(map(lambda x: x * 2, lista))}")
print(f"zastosowanie funkcji map(){list(map(lambda x: x * 3, lista))}")
print(f"zastosowanie funkcji map(){list(map(lambda x: x * 4, lista))}")
print(f"zastosowanie funkcji map(){list(map(lambda x: x * 5, lista))}")
print(f"zastosowanie funkcji map(){list(map(lambda x: x * 6, lista))}")

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)

print(f"Zastosowanie filter(){list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(){list(filter(lambda x: x < 4, lista))}")
print(f"Zastosowanie filter(){list(filter(lambda x: x < 5, lista))}")
print(f"Zastosowanie filter(){list(filter(lambda x: x < 6, lista))}")
print(f"Zastosowanie filter(){list(filter(lambda x: x > 20 and x < 200, lista))}")
print(f"Zastosowanie filter(){list(filter(lambda x: x > 20 and x < 200, lista))}")

#####################
print(40*"#")
#####################
