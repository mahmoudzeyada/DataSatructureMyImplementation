import random


def insertion_sort(a):
    for i in range(len(a)):
        value = a[i]
        hole = i
        while (hole > 0 and a[hole-1] > value):
            a[hole] = a[hole-1]
            hole -= 1
        a[hole] = value
    return a


print(insertion_sort(([random.randint(0, 1000) for _ in range(0, 1000)])))
