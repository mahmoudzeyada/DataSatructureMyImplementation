# the worst case for that data structure is O(m*f(m,n)) where m the number of union
# operations and the very slowly growing inverse of Ackermann’s function.
# In application α(m,n) <= 4 SO WE CAN CONSIDER IT  LINEAR  we can solve many
# problems with Bfs but it takes more memory than disjoint set so it is fast and light data structure


parents = [0]*6
ranks = [0]*6


def make_set(i):
    parents[i] = i
    ranks[i] = 0


def find_set(i):
    if i != parents[i]:
        parents[i] = find_set(parents[i])
    return parents[i]


def union(x, y):
    x_set = find_set(x)
    y_set = find_set(y)

    if ranks[x_set] > ranks[y_set]:
        parents[y_set] = x_set
    else:
        parents[x_set] = y_set

        if ranks[x_set] == ranks[y_set]:
            ranks[y_set] += 1


for i in range(0, 6):
    make_set(i)

union(1, 3)
union(4, 1)
union(2, 0)
union(1, 2)


[print(index, value) for index, value in enumerate(parents)]
