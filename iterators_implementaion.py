import time


class Series:

    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration

        else:
            self.current += 1
            return self.current-1


def custom_for_loop(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while(done_looping is not True):
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        print(action_to_do)


series = Series(1, 10)

custom_for_loop(series, "yes")


def generates(low, high):
    while low < high:
        yield low
        low += 1


# nums = generates(1, 10)
# for i in nums:
#     print(i)

squraes = (nums*2 for nums in range(5))

# old code

readings = [i for i in range(5)]


def old():
    current = readings[0]
    differences = []
    for next_item in readings[1:]:
        differences.append(next_item - current)
        current = next_item


t0 = time.time()
old()
t1 = time.time()
print("old", t1-t0)
# new code


def with_next(iterable):
    iterator = iter(iterable)
    current = next(iterator)
    for next_item in iterator:
        yield current, next_item
        current = next_item


t0 = time.time()
l = [next_item - current for next_item, current in with_next(readings)]
t1 = time.time()

print("iterator", t1-t0)
