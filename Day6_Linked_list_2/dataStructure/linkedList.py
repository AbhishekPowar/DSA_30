class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

    def displayTillEnd(self):
        cur = self
        ans = []
        while cur:
            ans.append(str(cur.val))
            cur = cur.next
        if ans:
            print('   ->   '.join(ans))
        else:
            print('<empty>')


class singlyLinkedList():
    def __init__(self):
        self.head = None

    def push(self, val, next=None):
        cur = self.head
        if cur == None:
            self.head = Node(val, next)
        else:
            while cur.next:
                cur = cur.next
            cur.next = Node(val, next)

    def __repr__(self):
        ans = []
        cur = self.head
        while cur:
            ans.append(str(cur))
            cur = cur.next
        if len(ans):
            return '   ->   '.join(ans)
        else:
            return f'<empty>'

    def __len__(self):
        if self.head == None:
            return 0
        else:
            count = 0
            cur = self.head
            while cur:
                count += 1
                cur = cur.next
            return count

    def pop(self):
        if self.head:
            if self.head.next == None:
                self.head = None
            else:
                cur = self.head
                while cur.next.next:
                    cur = cur.next
                last = cur.next
                del last
                cur.next = None

    def delFirst(self):
        if self.head:
            cur = self.head
            del cur
            self.head = self.head.next

    @staticmethod
    def display(node):
        cur = node
        ans = []
        while cur:
            ans.append(str(cur.val))
            cur = cur.next
        print(' -> '.join(ans))
