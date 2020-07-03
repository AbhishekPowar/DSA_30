# 2__Find_middle_of_LinkedList3_

from dataStructure.linkedList import singlyLinkedList


def middleNode(head):
    def middle(head):
        if head == None:
            return -1
        elif head.next == None:
            return 0
        else:
            cur = head
            length = 0
            while cur:
                length += 1
                cur = cur.next
            return length//2

    def nthNode(head, n):
        cur = head
        while n:
            n -= 1
            cur = cur.next
        return cur

    n = middle(head)
    if n == -1:
        return head
    ans = nthNode(head, n)
    return ans


if __name__ == "__main__":
    ll = singlyLinkedList()
    for i in range(1, 9):
        ll.add(i)
    mNode = middleNode(ll.head)
    mNode.displayTillEnd() 

     