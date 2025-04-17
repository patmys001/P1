# funckje zwracają wynik
# return
def dodaj(a, b):
    return a + b


def odejmij(a, b, c=5):
    return a - b - c


def odejmij2(a, b, ):
    return a - b


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(5, 4))
print(odejmij(10, 6))
print(odejmij(4, 100))
print(odejmij(10, 2, c=5))
print(odejmij2(5, 3))
print(oblicz_vat(1000, 15))
print(oblicz_vat(1000))
print(oblicz_vat(vat=15, kwota=1000))

zm=oblicz_vat(1000)
if zm==1230:
    print("Ok")
    print(type(zm))
print(dodaj(5,6)+ dodaj(4,5))
