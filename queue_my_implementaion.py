class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def dequeue(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]


q = Queue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek())

q.enqueue(4)
print(q.dequeue())
print(q.peek())
