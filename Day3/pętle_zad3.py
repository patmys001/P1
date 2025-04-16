# pętla while - sterowana warunkiem
# while True: -> pętla nieskończona

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break
print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("komuniakat 3!!!")

# password = input("Podaj hasło:")
# while password != "secret":
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło OK !!!")
#
# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append((int(wej)))
# print(lista)
# print(lista_int)
print(30 * "#")
######################
my_list =[1,5,2,3,5,4,5,6,5,5]
element_to_remove = 5
print(my_list)
while element_to_remove in my_list:
    my_list.remove(element_to_remove)
print(my_list)

my_list =[1,5,2,3,5,4,5,6,5,5]
print(dict.fromkeys(my_list))
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)
print(30 * "#")
############
