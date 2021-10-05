# Implement_Queue_using_Stack

from P1_Implement_Stack_Using_Array import Stack


class Queue():
    def __init__(self):
        self.inputStack = Stack()
        self.outputStack = Stack()

    def push(self, data: int) -> None:
        self.inputStack.push(data)

    def pop(self) -> None:
        if not self.outputStack.isEmpty():
            self.outputStack.pop()
        else:
            # Copy input stack to outputStack
            self.copyStack()
            self.outputStack.pop()

    def peek(self) -> int:
        if not self.outputStack.isEmpty():
            return self.outputStack.peek()
        else:
            self.copyStack()
            return self.outputStack.peek()

    def isEmpty(self) -> bool:
        return self.inputStack.isEmpty() or self.outputStack.isEmpty()

    def copyStack(self):
        while not self.inputStack.isEmpty():
            self.outputStack.push(self.inputStack.peek())
            self.inputStack.pop()

    def __repr__(self):
        out = str(self.outputStack)[1:-1].split(',')
        out.reverse()
        pout = []
        if out != "['']":
            pout = list(map(int, out))

        return f'outputStack={pout} inputStack={self.inputStack}'

    def print(self):
        print(f'{self.outputStack} {self.inputStack}')


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.pop()
    print('queue peek ', q.peek())
    q.push(4)
    print(q)
