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
#-----------------------------
lista_15 = list(range(15))
print(lista_15)
print(lista_15[0:15:2]) #start:stop:krok
print(list(range(0,15,2)))
print(lista[::-1]) #odwrócenie listy
print("//----------------")

