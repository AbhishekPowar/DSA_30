# https://leetcode.com/problems/copy-list-with-random-pointer/
#7__Clone_a_Linked_List_with_random_and_next_pointer_

from dataStructure.linkedList import singlyLinkedList as sLL, Node

def copyRandomList(head):
    if not head:
        return head
    newhead = Node('-1')

    hmap  = {}
    hmap[None]=None

    nh = newhead
    h = head
    while h:
        cur  = Node(h.val) 
        hmap[h] = cur
        nh.next = cur
        nh = cur
        h=h.next

    h =head
    nh = newhead.next
    while h:
        nh.random = hmap[h.random]
        h = h.next
        nh = nh.next

    return newhead.next

# if __name__ == "__main__":
#     start = 1 
#     end=5 
#     k = 6 
#     ll = sLL()
#     for i in range(start, end+1):
#         ll.push(i)
#     l2 = copy(ll.head)
#     l2.displayTillEnd()