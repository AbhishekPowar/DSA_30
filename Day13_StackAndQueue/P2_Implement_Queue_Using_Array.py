# Implement_Queue


class Queue:
    def __init__(self, size=8, isExpandable=False):
        self.isExpandable = isExpandable
        self.maxSize = size
        self.dataArr = [0] * self.maxSize
        self.start = -1
        self.end = -1
        self.len = 0

    def getSize(self):
        return self.maxSize

    def __len__(self):
        return self.len

    def push(self, data):
        if self.len < self.maxSize:
            if self.end == self.maxSize-1:
                self.__rotateDataArray()
            self.dataArr[self.end+1] = data
            self.end += 1
            self.len += 1
        else:
            if self.isExpandable:
                if self.start != -1:
                    self.__rotateDataArray()
                temp = self.dataArr
                self.dataArr = [0] * (self.maxSize * 2)
                self.maxSize *= 2
                for idx, x in enumerate(temp):
                    self.dataArr[idx] = x
                self.push(data)
            else:
                print(f"Queue full, cannot insert {data}")
            # raise Exception("Queue full")

    def __rotateDataArray(self):
        for idx in range(0, self.len):
            self.dataArr[idx] = self.dataArr[self.start+idx+1]
        self.start = -1
        self.end = self.len - 1

    def pop(self):
        if self.len > 0:
            self.start += 1
            self.len -= 1
            return self.dataArr[self.start-1]
        else:
            print("Queue empty")
            # raise Exception("Queue empty. Cannot pop")

    def isEmpty(self):
        return self.len == 0

    def peek(self):
        if self.len > 0:
            return self.dataArr[self.start]
        else:
            print("Queue empty")
            # raise Exception("Queue empty. Cannot pop")

    def print(self):
        print([self.dataArr[x] for x in range(self.start+1, self.end+1)])

    def __repr__(self):
        return f'{[self.dataArr[x] for x in range(self.start+1, self.end+1)]}'


if __name__ == "__main__":
    qu = Queue(size=4, isExpandable=False)
    print(f'isEmpty = {qu.isEmpty()}')
    qu.pop()
    print(f'getSize = {qu.getSize()}')

    [qu.push(x) for x in range(1, 5)]
    print(f'len = {len(qu)}')
    qu.pop()
    qu.push(8)
    print(f'peek = {qu.peek()}')
    qu.print()

