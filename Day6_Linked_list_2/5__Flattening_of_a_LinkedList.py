# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# 5__Flattening_of_a_LinkedList
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:

# The multilevel linked list in the input is as follows:


def flatten(head):
    def clean(node):
        cur = node
        if cur.child:
            nxt = cur.next
            nh, nl = clean(cur.child)
            cur.next = nh
            nl.next = nxt
            nh.prev = cur
            if nxt:
                nxt.prev = nl
            cur.child = None
        last = cur
        while cur:
            if cur.child:
                nxt = cur.next
                nh, nl = clean(cur.child)
                cur.next = nh
                nl.next = nxt

                nh.prev = cur
                if nxt:
                    nxt.prev = nl
                cur.child = None
            last = cur
            cur = cur.next
        return node, last
    if head:
        h, t = clean(head)
    return head
