# https://leetcode.com/problems/add-two-numbers/solution/
# 6__Add_two_numbers_as_LinkedList

'''Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807'''

from dataStructure.linkedList import singlyLinkedList as sLL, Node as ListNode


def addTwoNumbers(l1, l2):
    newhead = ListNode('head')
    cur = newhead
    carry = 0
    while l1 or l2 or carry:
        summ = carry
        if l1:
            summ += l1.val
            l1 = l1.next
        if l2:
            summ += l2.val
            l2 = l2.next

        cur.next = ListNode(summ % 10)
        carry = summ//10
        cur = cur.next

    newhead.displayTillEnd()


if __name__ == "__main__":
    l1 = sLL()
    l2 = sLL()
    n1 = [6, 4, 3]
    n2 = [5, 6, 7, 8]
    for i in n1:
        l1.push(i)
    for j in n2:
        l2.push(j)
    addTwoNumbers(l1.head, l2.head)
