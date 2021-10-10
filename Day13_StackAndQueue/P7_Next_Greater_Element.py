# Next_Greater_Element

from collections import deque


class Stack(deque):
    def push(self, data):
        self.append(data)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return len(self) == 0


def nextGreatestRight(ar):
    N = len(ar)
    solution = [0] * N

    s = Stack()
    for idx in range(N-1, -1, -1):
        while not s.isEmpty() and s.peek() < ar[idx]:
            s.pop()
        if s.isEmpty():
            solution[idx] = -1
        else:
            solution[idx] = s.peek()
        s.push(ar[idx])
        print(s)
    return solution


if __name__ == "__main__":
    ar = [1, 3, 2, 4]
    expectedSolution = [3, 4, 4, -1]
    print(f'{ar=}')
    print(f'{expectedSolution=}')
    sol = nextGreatestRight(ar)
    print(sol)
