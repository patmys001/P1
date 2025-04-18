# class - element programowania obiektowego
# klasa - szablon
# metody to funkcje w klasie
# dandermethod __init__
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# PascalCase

class Human:
    """"
    klasa Human w Python
    """
    imie = ""
    wiek = None
    plec = "k"
    def powitanie(self):
        print(f"Nazywam się{self.imie}")
    def wiekowosc(self):
        print(f"Mój wiek to{self.wiek}")


cz1=Human()
print(cz1)
print(40*"^")
print(Human.__doc__)
print(print.__doc__)

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
print(40*"^")
cz1.wiek=45
cz1.imie="Anna"

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
print(40*"^")

cz1.powitanie()
cz1.wiekowosc()
print(40*"^")