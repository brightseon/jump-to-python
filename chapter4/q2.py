from ast import arg


def avg(*args):
    total = 0

    for i in args:
        total += i

    return total / len(args)


print(avg(1, 2, 3))
