# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# 4__Remove_N-th_node_from_back_of_LinkedList

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

from dataStructure.linkedList import singlyLinkedList as sLL, Node

# 2 passes


def delNth(head, n):
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next
    if n < length:
        length -= n+1
        cur = head
        while length:
            length -= 1
            cur = cur.next
        nxt = cur.next
        cur.next = nxt.next
        del nxt
    elif n == length:
        head = head.next
    return head

# single pass


def removeNthEnd(head, n):
    cur = head
    slow = cur
    fast = cur
    while n:
        n -= 1
        last = fast
        fast = fast.next
        if fast == None:
            break
    if n == 0 and not fast:
        head = head.next
    elif fast:
        fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
    return head


if __name__ == "__main__":
    ll = sLL()
    for i in range(1, 11):
        ll.push(i)

    # ll.head = delNth(ll.head, 1)
    ll.head = removeNthEnd(ll.head, 10000)
    print(ll)
