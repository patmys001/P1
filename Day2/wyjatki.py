# Wyjątki - błędy podczas wykonywania programu

# print(5 / 0) # błąd
try:
    # print(5 / 0)
    # print("a"*"23")
    wynik = 98 / 33
    # raise KeyError("Brak klucza")
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Błąd", e)
else:
    print("Wynik", wynik)
finally:
    print("Koniec działania")
print("Program nadal działa")
