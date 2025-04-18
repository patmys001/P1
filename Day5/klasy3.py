# klasy 3
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa  opisująca ptaka w pythonie

    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością ", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko kok ko kok ok oko kok")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po Klasie Ptak
    """

    def wydaj_odglos(self):
        print("kier kier kier")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# or1 = Ptak("Orzel", 45)
# or1.latam()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()
kur2 = Kura("Kura")
kur2.latam()
kur2.wydaj_odglos()
or2 = Orzel("Orzel", 45)
or2.latam()
or2.wydaj_odglos()
# sowa=Sowa("Sowa",65)

# polimorfizm
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
kur2.wydaj_odglos()

