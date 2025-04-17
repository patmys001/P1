# funkcja - wykonanie fragmentu kodu wielokrotnie
# deklaracja funckji
#####################################################
a = 8
b = 6


def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# użycie/uruchominie
dodaj()
dodaj2(10, 50)
odejmij(10, 5, 3)
odejmij(10, 5)
odejmij(c=5, b=7, a=78)

# argumenty pozycyjne i arugmenty po nazwie
# miesznae
odejmij(1, 9)
dodaj2(1, 10)
# najpier pozycja potem po nazwie
print(dodaj())
print(dodaj2(56, 78) * dodaj())

print(30 * "#")
