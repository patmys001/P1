def all_params(a, b, c=42, d=256):
    print(f"{a},{b}")
    print(f"{c},{d}")


all_params(1, 2)
all_params(1, 2, 3)
all_params(1, 2, 3, 4)
all_params(1, 2, c=3, d=4)
# / powoduje, że a ib mogą być przekazane tylko do pozycji !!!
all_params(a=1, b=2, c=3, d=4)

print(30 * "#")
def all_params(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a},{b}")
    print(f"{c},{d}")
    print(f"{args},{kwargs}")
all_params(1,2)
all_params(1,2,c=3)
all_params(1,2,3,4,5,6,7,8,)
all_params(1,2,3, 2,3,4,5,6)
all_params(1,2,3, 2,3,4,5,6,d=100)
all_params(1,2,3, 2,3,4,5,6,d=100,name="Patryk")
all_params(1,2,3, 2,3,4,5,6,d=100,name="Patryk",a=7)




