# instrukcje warunkowe - instrukcje sterowania przepływem programu
# if


odp = True
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
print("Dalsza część programu")

if odp:
    print("dane zostały pobrane")
odp = "Patryk"
if odp == "Patryk":
    print("Nadal Patryk")
odp = 0
if odp:
    print("Działa")
else:
    print("Zero-.False")

print("//----------------")
a = ("Patryk")
if len(a) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")

# operator morsa , walrus
print("//----------------")
if (n := len(a)) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")

print("//----------------")

# ctr +/ i komentuje całość zaznaczoną

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 39999:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
#
# else:
#     podatek = 0.9
# print(f"Podatek wynosi {podatek * zarobki} pln.")

print("//----------------")

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi {rabat}")
rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

###########################
# napisac program test z ...
print("Czy jesteś wysoki?")
h = 185
if h > 185:
    odp = True
else:
    odp = False

