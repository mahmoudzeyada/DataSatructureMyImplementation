def parent(i):
    return i/2


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def heapify(a, i):
    ''' function for mantaing max heap property  '''
    l = left(i)
    r = right(i)

    if l <= len(a)-1 and a[i] < a[l]:
        largest = l
    else:
        largest = i

    if r <= len(a)-1 and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest)
    return a


def build_max_heap(a):
    ''' function for building max heap binary tree '''
    for i in range(int(len(a)/2)):
        heapify(a, i)
    return a


print(build_max_heap([3, 9, 8, 2, 2, 7]))
