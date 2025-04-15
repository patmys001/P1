tekst = 'witaj świecie'
print(tekst)
print(type(tekst))

# teksty są niemutowalne

tekst.upper()
print(tekst.upper())
upper_case = tekst.upper()
print(upper_case)

print(tekst.capitalize())
print((tekst.lower()))
print(tekst.removeprefix("witaj"))
print(tekst.removesuffix("świecie").strip())

encoded_s = tekst.encode("utf-8")
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))

# indeksy sa od 0

print(tekst[4])
print(tekst.count("j"))
print(tekst.count("j", 0, 4))

imie = ("patryk")
print(imie)
print("Imie", imie)
starszy = "Witaj %s!"
print(starszy % imie)
#tekst_format = f"Mam na imie {imie} i lubie pythona"
tekst_format = f"\t Mam na imie {imie}\n i lubie pythona. \b"
print(tekst_format)

print("Witaj {}!".format(imie))

print("""tekst wielolinijkowy
wiesz ? XDDD""")
