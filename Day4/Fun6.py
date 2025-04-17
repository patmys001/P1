# stworzyć funkcję obliczająca średnią
# * - przyjmuje wiele argumentów pozycyjnych
from itertools import count


def liczby(name=None, *cyfry):  # rozpakowanie krotki
    print(cyfry)
    try:
        count = len(cyfry)
        suma = 0
        for c in cyfry:
            suma += c
        avg = suma / count

    except Exception as e:
        print("Błąd:", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi: {avg}")
    finally:
        print("Nastepne obliczaenie")


liczby()
liczby(1, 2, 3, 4, 4, 5, 3, 3, 3, 2, 1)
liczby("Radek", 1, 2, 3, 6, 6, 6)

