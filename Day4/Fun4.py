# funkcja wew. zagnieżdżona
def fun1():
    print("to jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2() #zwraca wyynik
    return fun2


xfun = fun1()
print(xfun)
print(type(xfun))
xfun()
xfun()
xfun()
xfun()
