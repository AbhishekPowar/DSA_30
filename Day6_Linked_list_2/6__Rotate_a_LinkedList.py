#6__Rotate_a_LinkedList
from dataStructure.linkedList import singlyLinkedList as sLL, Node

def rotateRight(head,k):
    if k and head:
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next

        k = k%length
        if k==0:
            return head
        else:
            last = head
            while k:
                k-=1
                last = last.next
            newlast = head    
            while last.next:
                last = last.next
                newlast = newlast.next
            newHead  =newlast.next
            newlast.next = None
            last.next = head
            head = newHead
            return head
    return head


if __name__ == "__main__":
    start = 1
    end=5
    k = 6
    ll = sLL()
    for i in range(start, end+1):
        ll.push(i)
    print(ll) 
    ll.head = rotateRight(ll.head,k)
    print(ll) 