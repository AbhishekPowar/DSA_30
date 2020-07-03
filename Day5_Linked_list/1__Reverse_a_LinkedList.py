# https://leetcode.com/problems/reverse-linked-list/
# 1__Reverse_a_LinkedList
from dataStructure.linkedList import singlyLinkedList, Node


class sLL(singlyLinkedList):
    def recur(self):
        cur = self.head
        if self.head == None or self.head.next == None:
            return self.head
        else:
            def reverse(node):
                if node.next == None:
                    return node
                nxt = node.next
                rem, nxt.next = reverse(nxt), node
                return rem
            cur = self.head
            self.head = reverse(self.head)
            cur.next = None

    def rev(self):
        prev = None
        cur = self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev


ll = sLL()
for i in range(1, 6):
    ll.add(i)
print(ll)
# ll.rev()
ll.recur()
print(ll)
