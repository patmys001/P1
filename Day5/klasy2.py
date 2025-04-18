# klasy 2
class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizujaca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def wiekowosc(self):
        print(f"Mój wiek to {self.wiek}")

    def wysokosc(self):
        print(f"Mój wzrost {self.wzrost} wzrostu")

    def moja_plec(self):
        print(f"Moja plec to {self.plec}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Anna", 37, 170, "Kobieta")
cz1.powitanie()
cz1.wiekowosc()
cz1.wysokosc()
cz1.moja_plec()
cz2 = Human("Wojtek", 43, 187, "m")
print(40*"^")
cz1.ruszaj()
cz2.ruszaj()
