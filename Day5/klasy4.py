# klasy 4
class Car:
    """
    Klasa opisująca samochó w python
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizując
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Jade z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Multipla", 2025)
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)
car1.licznik()
car1.hamuj()
car1.licznik()
