# Next_Smaller_Element

from collections import deque


class Stack(deque):
    def push(self, data):
        self.append(data)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return len(self) == 0


def nextSmallestLeft(ar):
    N = len(ar)
    solution = [0] * N

    s = Stack()
    for idx in range(N-1, -1, -1):
        while not s.isEmpty() and s.peek() > ar[idx]:
            s.pop()
        if s.isEmpty():
            solution[idx] = -1
        else:
            solution[idx] = s.peek()
        s.push(ar[idx])
        print(s)
    return solution


if __name__ == "__main__":
    ar = [5, 4, 7, 1, 8, 2]
    expectedSolution = [4, 1, 1, -1, 2, -1]
    print(f'{ar=}')
    print(f'{expectedSolution=}')
    sol = nextSmallestLeft(ar)
    print(sol)
