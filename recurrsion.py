y = ["a", "b", "c"]


def recurrsion_loop(y):
    if len(y) > 0:
        print(y[len(y)-1])
        y = y[0:-1]
        recurrsion_loop(y)


def f_e_loop():
    for x in y:
        print(x)


def not_recurssion():
    print("hello")
    not_recurssion()

recurrsion_loop(y)