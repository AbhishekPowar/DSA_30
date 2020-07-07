# https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
# 3__Reverse_a_LinkedList_in_groups_

from dataStructure.linkedList import singlyLinkedList as sLL, Node


def arrAns(n, g):
    def rev(arr, start, end):
        if start:
            arr[start:end] = arr[end-1:start-1:-1]
        else:
            arr[start:end] = arr[end-1::-1]

    arr = [i for i in range(1, n+1)]
    print(arr)
    s = 0
    for s in range(0, len(arr)+1, g):
        rev(arr, s, s+g)
    print(arr)


def rev(node, k):
    count = k
    temp = node
    while temp and count:
        temp = temp.next
        count -= 1

    if count == 0:
        count = k
        prev, cur = None, node
        while count and cur:
            count -= 1
            next, cur.next = cur.next, prev
            prev, cur = cur, next
        if cur:
            node.next = rev(cur, k)
        return prev
    else:
        return node


if __name__ == "__main__":
    n = 9
    g = 3
    arrAns(n, g)

    ll = sLL()
    for i in range(1, n+1):
        ll.push(i)
    ll.head.displayTillEnd()
    ll.head = rev(ll.head, g)
    print(ll)
