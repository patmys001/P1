# od pythona 3.10
# match case - to jest inny IF
lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("znam pythona")
    case "java":
        lista.append("znam jave")
    case _:  # taki else jak w IF
        print("inny")
print(lista)
print(30 * "#")
