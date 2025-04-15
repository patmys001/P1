# FORMATY
import sys

user = "Patryk"  # string
wiek = 30  # int
wersja = 3.9000001  # float
print(type(wersja))  #
print(sys.float_info)
liczba = 72647624678267842  # int
print("Witaj %s masz teaz %d lat." % (user, wiek))  # poprawne typy
# print("Witaj %d masz teaz %s lat." % (user, wiek)) # sprawdza typy i dlatego nie przchodzi
print("Witaj %(user)s. Jak się czujesz %(user)s?" % {"user": user})
print("Witaj %(user)s. Co pijemy %(user)s?" % {"user": user})
print("Witaj {}, masz teraz {} lat.".format(user, wiek))
print(f"Witaj {user}, masz teraz {wiek} lat XD!")

print("Używamy wersji python %i" % 3)
print("Używamy wersji python %f" % 3)
print("Używamy wersji python %.1f" % 3)
print("Używamy wersji python %.2f" % 3)
print("Używamy wersji python %.0f" % 3)
print("Używamy wersji python %.f" % 3)
print(f"Uzywamy wersji python {wersja}")
print(f"Uzywamy wersji python {wersja}.2f")
print(f"Uzywamy wersji python {wersja}.1f")

print(f"{user:>10}")  # jak w word wyrównanie
print(f"{user:<15}")  # jak w word wyrównanie
print(f"{user:^35}")  # jak w word wyrównanie

print(liczba)
print(f"Nasza duża luiczba {liczba:,}")
print(f"Nasza duża luiczba {liczba:_}")
print(f"Nasza duża luiczba {liczba:_}".replace("_", " "))

dane = 5000000000000000
dane =50_000_000_000
print(type(dane))
