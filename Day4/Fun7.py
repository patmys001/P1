def connect(**opcje):
    print(opcje)


connect()
connect(a=6)


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3)
all_args(a=7, b=8)
all_args(1, 2, 3, b="patryk")


