from ftplib import print_line

dictionary = {"Imie": "Patryk", "Nazwisko": "Mysliwiec"}
print(type(dictionary))
for i in dictionary:
    print(i)
print(30 * "#")
for v in dictionary.values():
    print(v)
print(30 * "#")
for i in dictionary.items():
    print(i)
print(30 * "#")
for k, i in dictionary.items():
    print(k, i)
print(30 * "#")
for k, i in dictionary.items():
    print(k, i, sep="=>")
print(30 * "#")

###########################

# słownik polsko - angielski
print("Słownik polsko-angielski")
pol_ang = {"kot": "cat"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)

print({value: key for key, value in pol_ang.items()}) # to jest to co wyżej tylko bardziej bo pythonowemu

print(30 * "#")
