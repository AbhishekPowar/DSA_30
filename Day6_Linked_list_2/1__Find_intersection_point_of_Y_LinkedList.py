# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
# 1__Find_intersection_point_of_Y_LinkedList

from dataStructure.linkedList import singlyLinkedList as sLL

# hashing solution
# Time O(m+n)
# Memory O(m+n)


def getIntersectionNode(A, B):
    d = {}
    cur = A
    while cur:
        d[cur] = 1
        cur = cur.next

    cur = B
    while cur:
        if cur in d:
            return cur
        else:
            d[cur] = 1
        cur = cur.next
    return None


if __name__ == "__main__":
    l1 = sLL()
    l2 = sLL()
    for i in range(10, 60, 10):
        l1.push(i)
    inter = None
    for j in range(1, 10, 1):
        l2.push(j)

    node = l1.head.next.next.next
    node.next = l2.head.next.next

    print(f'Linked list 1 :', l1)
    print(f'\nLinked List 2 :', l2)
    ans = getIntersectionNode(l1.head, l2.head)
    print(f'\nCommon part')
    ans.displayTillEnd()
