#TYPY PRYMITYWNE!!!!
wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float
print(temp)
print(type(temp))
print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # float
print(rok // wiek)  # część calkowita z dzielenia
print(rok % wiek)  # reszta z dzielenia
print(5 % 2)  # wynik 2 r 1

print(wiek ** rok)  # potęga wiek  do roku
print(len(str(wiek ** rok)))
# print(len(str(wiek ** rok ** 2)))

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - 5 * 43 + 4 / (2 + 4) / 2)

print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.4 + 0.5)
# decimal - pozwala ominąć błąd zakokrąglenia

print(f"sprawdzenie zmiennej {temp}{wiek}")
print(f"""
{temp}
{wiek}""")

# typ logiczny prawda fałsz
# True False

czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # bool
print(int(czy_znasz_pythona))
print(int(False))
print(bool(1))
print(bool(0))
print("//----------------")
print(bool(100))
print(bool(-100))
print(bool("Patryk"))
print(bool("0"))

print(bool(""))
print(bool(None))  # stan nie okreslony, odpowiedni null (None zawsze z dużej litery)
print("//----------------")
# and -i
print(True and False)
print(False and False)
print(False and True)
print(True and True)
print("//----------------")
# or - lub
print(True or False)
print(False or False)
print(False or True)
print(True or True)
print("//----------------")
# not - negacja
print(not True)
print(not False)
print("//----------------")
a = 8
b = 6
print(f"Porównanie {a} > {b}={a > b}")
print(f"Porównanie {a} < {b}={a < b}")
print(f"Porównanie {a} >= {b}={a >= b}")
print(f"Porównanie {a} => {b}={a <= b}")
print(f"Porównanie {a} == {b}={a == b}")
print(f"Porównanie {a} != {b}={a != b}")
print(f"Porównanie {a>=b =}")
print("//----------------")
