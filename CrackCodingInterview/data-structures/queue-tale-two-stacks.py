class Stack(object):

    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        try:
            val = self.storage.pop()
        except IndexError:
            return None
        else:
            return val

    def empty(self):
        return len(self.storage) == 0

    def tos(self):
        if len(self.storage):
            return self.storage[len(self.storage)-1]
        else:
            return None


class MyQueue(object):

    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()

    def peek(self):
        if self.dequeue.empty():
            self._move(self.enqueue, self.dequeue)
        return self.dequeue.tos()

    def pop(self):
        if self.dequeue.empty():
            self._move(self.enqueue, self.dequeue)
        return self.dequeue.pop()

    def put(self, value):
        self.enqueue.push(value)

    def _move(self, stack_from, stack_to):
        while True:
            val = stack_from.pop()
            if val is None:
                break
            stack_to.push(val)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
