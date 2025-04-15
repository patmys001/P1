# zbiór (set) - przechouje inikalne wartości
# nie zachowuje koelności przy dodawaniu elementów
# nie posiada indeksu
print("//----------------")
lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)
print(type(zbior))
print("//----------------")
# pusty zbiór
zb2 = set()
print(type(zb2))
print(zb2)
# dodanie elementów do zbioru
zbior.add(33)
zbior.add(32)
zbior.add(17)
zbior.add(19)
zbior.add(24)
print(zbior)
# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)
print(id(zbior))
print("//----------------")
# pop()
print(zbior.pop())  # usuwa peirwszy element ze zbioru
zmienna = zbior.pop()
print("Usunieto", zmienna)
print("//----------------")
zbior_copy = zbior.copy()
print(zbior_copy)
print(id(zbior_copy))
print("//----------------")
# operacje na zbiorach
zbior_2 = {667, 11, 44, 12, 34, 18, 52, 667, 62}
print(type(zbior_2))
print(zbior_2)
print("//----------------")
# suma zbiorów
print(zbior | zbior_2)
print(zbior.union((zbior_2)))
print("//----------------")
# częśc wspolna
print(zbior & zbior_2)
print(zbior_2.difference(zbior))
print(zbior_2.difference((zbior)))
print("//----------------")
# łączy zbiory
zbior.update(zbior_2)
print(zbior)

krotka = tuple(zbior)
print(krotka)
lista = list(zbior)
print(lista)
print("//----------------")
# sprawdzenie czy dany element isntieje w danje kolekcji
print(667 in zbior)
print(777 in lista)
print(777 in krotka)

