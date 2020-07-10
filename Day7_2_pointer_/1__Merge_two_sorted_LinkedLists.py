# https://leetcode.com/problems/merge-two-sorted-lists/
# 1__Merge_two_sorted_LinkedLists


def mergeTwoLists(l1, l2):
    head = ListNode('head')
    cur = head
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return head.next
