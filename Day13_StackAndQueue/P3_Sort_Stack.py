# Sort Stack

from P1_Implement_Stack_Using_Array import Stack

def SortStack(s):
    if s.length() > 1:
        temp = s.pop()
        SortStack(s)
        smartInsert(s, temp)


def smartInsert(s, data):
    if s.length() == 0 or s.peek() < data:
        s.push(data)
    else:
        temp = s.pop()
        smartInsert(s, data)
        s.push(temp)


if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(9)
    s.push(4)
    s.print()
    SortStack(s)
    s.print()
