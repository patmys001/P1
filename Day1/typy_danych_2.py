# Typy Kolekcje - lista
# kolekcje przechowują wiele elementów  róznych typów naraz
# lista zachowuje kolejność przy dodawaniu
print("//----------------")
# pusta lista
lista = []
print(lista)
print(type(lista))

pusta_lista = list()
print(pusta_lista)
print(type(pusta_lista))

# append() - dodanie elementów do listy
lista.append("Patryk")
lista.append("Tomek")
lista.append("Filip")
lista.append("Emilia")
lista.append("Agnieszka")
print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
# rint(lista[10]) out of range
print(len(lista))
print(len(lista) - 1)
print(lista[-1])
print(lista[-3])
print(lista[-2])
print("//----------------")
# slicowanie - fragemnt listy
print(lista[0:3])
print(lista[1:4])
print(lista[2:])
print(lista[2:5])
print(lista[2:15])
print("//----------------")
print(lista[:])
print(lista[2:2])
print(lista[2:3])
print(lista[10:23])
print("//----------------")
print(lista[-2:0])
print(lista[0:-2])
print("//----------------")
# -----------------------------
lista_15 = list(range(15))
print(lista_15)
print(lista_15[0:15:2])  # start:stop:krok
print(list(range(0, 15, 2)))
print(lista[::-1])  # odwrócenie listy
print("//----------------")

# nadpisanie elemntu w liście
lista[3] = "Roman"
print(lista)
# dopisanie do listy na wskazanym indeksie
lista.insert(1, "Wojtek")
print(lista)
print("//----------------")
lista.insert(3, "Sabina")
print(lista)
print("//----------------")
lista.insert(15, "Tadeusz")
print(lista)
# sprawdzenie numeru indeksu
print((lista.index("Tadeusz")))
print("//----------------")
lista.append("Filip")
print(lista)
print(lista.index("Filip"))
print("//----------------")
numer_sabina = lista.index("Sabina")
print(numer_sabina)
# usunięcie lelemntu z listy
lista.remove("Sabina")
print(lista)
# usunieci po indeksie
lista.pop(4)
print(lista)
print(lista.pop(4))
print(lista.pop(-4))
print(lista)
print(lista.pop())  # usuwanie ostatniego elementu w liscie
print("//----------------")
print(lista)

print("//----------------")
a = 1
b = 3
a = b
print(f"{a=},{b=}")
b = 9
print(f"{a=},{b=}")
lista_2 = lista  # odpowiednik a=b, kopia adresu listy, referencji
lista_copy = lista.copy()  # kopia elementów listy
print(lista)
print(lista_2)
lista.clear()
print(lista)
print(lista_2)
print(lista_copy)
print(id(lista))
print(id(lista_2))
print(id(lista_copy))
print("//----------------")
liczby = [54, 999, 34, 22, 12, 34, 567]
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)
print("//----------------")
liczby = [54, 999, 34, 22, 12, 34, 567, "A"]
print(liczby)
print(type(liczby))
# liczby.sort() # nie pójdzie bo różne typy danych
print(liczby)
print("//----------------")
print(lista_copy)
lista_copy.sort()
print(lista_copy)
lista_copy.sort(reverse=True)
print(lista_copy)
lista_copy.reverse()
print(lista_copy)
print("//----------------")
liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)
print("//----------------")
# rozpakowanie sekwencji
tekst = "Python on."
lista1 = list(tekst)
print((lista1))
lista2=[tekst]
print(lista2)
krotka=tuple(lista_copy)
print(type(krotka))
print(krotka)