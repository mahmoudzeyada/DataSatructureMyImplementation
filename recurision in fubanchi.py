
dist = {}


def rec(n):
    if n == 1 or n == 0:
        return n
    return rec(n-1)+rec(n-2)


print(rec(55))
