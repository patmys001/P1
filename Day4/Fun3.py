a = 10
b = 10


def dodaj():
    a = 7
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # uzyj globalnej a
    a = 9
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalne)")
dodaj()
print(f"Wartość a z góry {a=} (globalne)")
dodaj2()
print(f"Wartość a z góry {a=} (globalne)")
dodaj3()
print(f"Wartość a z góry {a=} (globalne)")
dodaj2()
print(f"Wartość a z góry {a=} (globalne)")
