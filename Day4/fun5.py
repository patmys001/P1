# stworzyć funkcję kantor
# ma miec dwie funkcje wewnętrzne eur i usd
# w zależności od parametru ma zwracać jedną z tych funkcji
# przelicz waluty

# def kantor():
#     print("Wymiana")
#
#     def euro():
#         e = 4.5
#         print(e)
#
#     euro()
#
#     def usd():
#         u = 3.9
#         print(u)
#
#     usd()
#
#
# wymiana = kantor()
# print(wymiana)


def kantor(waluta):
    def usd(kwota):
        print(f"Wymieniam dolary {3.77 * kwota}")

    def eur(kwota):
        print(f"Wymieniam deuro {4.28 * kwota}")

    if waluta == "USD":
        return usd
    else:
        return eur


kantor_eur = kantor("eur")
kantor_eur(1000)
kantor_eur(13000)

kantor_usd=kantor("USD")
kantor_usd(1000)
kantor_usd(13000)
