# random  :D - operacje na liczbach losowych
import random

print(random.randint(1, 100))
print(random.randrange(1, 100))
print(random.randrange(5))
print(random.random())
print(random.random() * 9)

# lista = [67, 45, 32, 68, 69, 98, 42]
print(30 * "#")

# print(random.randrange(1, 49))
# maszyna = random.randrange(1,49)
lista_wynik = []
lista_kul = list(range(1, 50))
print(lista_kul)
wynik = random.choice(lista_kul)
lista_kul.remove(wynik)
print(wynik)
lista_wynik.append(wynik)
print(lista_wynik)

print(random.choices(lista_kul, k=6))
print(random.sample(lista_kul, k=6))
print(random.sample(lista_kul, 6))

print(30 * "#")


print(30 * "#")
