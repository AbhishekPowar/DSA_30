# Implement_Stack_using_Queue

from collections import deque


class Queue(deque):
    def __init__(self):
        super().__init__()

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.popleft()

    def peek(self):
        if not self.isEmpty():
            return self[0]

    def isEmpty(self):
        return len(self) == 0


class Stack():
    def __init__(self):
        self.pushQueue = Queue()
        self.popQueue = Queue()

    def push(self, data):
        self.pushQueue.push(data)

    def peek(self):
        if not self.isEmpty():
            self.moveData()
            last = self.pushQueue.peek()
            self.popQueue.push(self.pushQueue.peek())
            self.pushQueue.pop()
            self.swapQueues()
            return last
        else:
            print('Stack is empty')

    def pop(self):
        if not self.isEmpty():
            self.moveData()
            self.pushQueue.pop()
            self.swapQueues()
        else:
            print('Stack is empty')

    def moveData(self):
        count = self.pushQueue.__len__()
        if not self.isEmpty():
            while count != 1:
                count -= 1
                self.popQueue.push(self.pushQueue.peek())
                self.pushQueue.pop()

    def swapQueues(self):
        self.pushQueue, self.popQueue = self.popQueue, self.pushQueue

    def isEmpty(self):
        return self.pushQueue.isEmpty() and self.popQueue.isEmpty()

    def __repr__(self):
        return f'{self.pushQueue} {self.popQueue}'


if __name__ == "__main__":
    s = Stack()
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.pop()
    print('isEmpty=', s.isEmpty())
    print('peek =', s.peek())
    s.pop()
    s.pop()
    s.pop()
    print('isEmpty=', s.isEmpty())
    print(s)
