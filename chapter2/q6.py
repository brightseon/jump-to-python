from audioop import reverse


def reverse_list(l):
    l.sort(reverse=True)
    return l

print(reverse_list([1, 3, 5, 4, 2]))