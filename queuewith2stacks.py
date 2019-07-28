class Queue:

    # this queue has an average O(1) in dequeue operation and enqueue
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def enqueue(self, a):
        self.__stack1.append(a)

    def dequeue(self):
        if len(self.__stack1) == 0:
            if len(self.__stack2) == 0:
                return False

        if len(self.__stack2) == 0:
            while(len(self.__stack1) != 0):
                a = self.__stack1.pop()
                self.__stack2.append(a)
        return self.__stack2.pop()


q = Queue()

for i in range(5):
    q.enqueue(i)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
