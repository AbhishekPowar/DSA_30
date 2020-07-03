#3__Merge_two_sorted_Linked_List

from dataStructure.linkedList import singlyLinkedList, Node

def mergeTwoLists(l1,l2):
    if l1 and l2:
        if l1.val < l2.val:
            newHead,l1 = l1,l1.next
        else:
            newHead,l2 = l2,l2.next 
        cur = newHead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next,l1 = l1,l1.next
            else:
                cur.next,l2 = l2,l2.next
            cur = cur.next
        cur.next=l2 if l2 else l1
        return newHead
    else:
        if l1:
            return l1
        elif l2:
            return l2
        else:
            return None
    

l1 = singlyLinkedList()
l2 = singlyLinkedList()
a = []
b = []
for i in a:
    l1.add(i)
for i in b:
    l2.add(i)

# print(l1)
# print(l2)

h = mergeTwoLists(l1.head,l2.head)
if h:
    h.displayTillEnd()
else:
    print('<empty>')   
