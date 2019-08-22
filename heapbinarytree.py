def parent(i):
    return int((i-1)/2)


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def heapify(a, i):
    ''' function for mantaing max heap property time-complexity = O(log n) but that it is that is optimized version  '''
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
    ''' function for building max heap binary tree time-complexity = O(n) '''
    for i in range(int(len(a)/2)):
        heapify(a, i)
    return a


def heap_extract_max(a):
    ''' function for extracting max  time-complexity = O(n log(n)) '''
    heap = build_max_heap(a)
    for _ in range(len(heap)):
        max_item = heap[0]
        print(max_item)
        heap[0], heap[-1] = heap[-1], heap[0]
        heap = heapify(heap[:-1], 0)


def heap_increase_key(heap, index, key):
    ''' function for increasing key time-complexity = O(log(n)) shifting up '''
    heap[index] = key
    while index > 0 and heap[parent(index)] < heap[index]:
        heap[parent(index)], heap[index] = heap[index], heap[parent(index)]
        index = parent(index)
    return heap


def heap_decrease_key(heap, index, key):
    ''' function for decreasing key time-complexity = O(log(n)) shifting down '''
    heap[index] = key
    return heapify(heap, index)


def max_heap_insert(heap, key):
    ''' function for inserting key time-complexity = O(log(n)) '''
    heap.append(float('-inf'))
    return heap_increase_key(heap, len(heap)-1, key)


def max_heap_delete(heap, index):
    ''' function for deleting key time-complexity = O(log(n)) '''
    heap[index] = heap[-1]
    return heapify(heap[:-1], index)


def build_max_heap_with_insert():
    ''' function for building key time-complexity = O(n log(n)) that uses shifting up  '''
    a = map(int, input("enter numbers to make heap:\t").split())
    heap = []
    for item in a:
        heap = max_heap_insert(heap, item)
    return heap


print(build_max_heap_with_insert())
