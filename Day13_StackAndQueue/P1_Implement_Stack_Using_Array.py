# Implement_Stack

class Stack:
    def __init__(self, size=8, isExpandable=False):
        self.isExpandable = isExpandable
        self.maxSize = size
        self.dataArr = [0] * self.maxSize
        self.top = -1
        self.len = 0

    def getSize(self):
        '''Internal array size'''
        return self.maxSize

    def length(self):
        '''Stack size'''
        return self.len

    def push(self, data):
        if self.top < self.maxSize-1:
            self.dataArr[self.top+1] = data
            self.top += 1
            self.len += 1
        else:
            if self.isExpandable:
                temp = self.dataArr
                self.dataArr = [0] * (self.maxSize * 2)
                self.maxSize *= 2
                for idx, x in enumerate(temp):
                    self.dataArr[idx] = x
                self.push(data)
            else:
                print(f"Stack full, cannot insert {data}")
            # raise Exception("Stack full")

    def pop(self):
        if self.top > -1:
            temp = self.dataArr[self.top]
            self.top -= 1
            self.len -= 1
            return temp
        else:
            print("Stack empty")
            # raise Exception("Stack empty. Cannot pop")

    def isEmpty(self):
        return self.top == -1

    def peek(self):
        if self.top > -1:
            return self.dataArr[self.top]
        else:
            print("Stack empty")
            # raise Exception("Stack empty. Cannot pop")

    def print(self):
        print([self.dataArr[x] for x in range(0, self.top+1)])

    def __str__(self):
        return f'{[self.dataArr[x] for x in range(0, self.top+1)]}'

if __name__ == "__main__":
    s = Stack(2, True)

    s.print()

    s.pop()

    s.push(11)
    s.push(12)
    s.push(12)
    s.push(12)
    s.push(13)
    print('Top =', s.peek())
    print('Size =', s.getSize())
    print('len =', s.length())

    s.print()

