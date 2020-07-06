# https://leetcode.com/problems/palindrome-linked-list/submissions/
# 2__Check_if_a_LinkedList_is_palindrome_or_not_

from dataStructure.linkedList import singlyLinkedList as sLL


def palindrome(head):
    stack = []
    cur = head

    # Calculating length
    length = 0
    while cur:
        length += 1
        cur = cur.next

    cur = head
    isOdd = length % 2
    length = length//2

    # Adding first half to stack
    while length:
        length -= 1
        stack.append(cur.val)
        cur = cur.next
    if isOdd:
        cur = cur.next

    # Poping remaining half if palindrome
    while cur:
        if cur.val == stack[-1]:
            stack.pop()
            cur = cur.next
        else:
            return False

    return True


if __name__ == "__main__":
    data = 'abcdcba'
    data = 'abcd'
    # data = 'abdcdba'

    ll = sLL()
    for i in data:
        ll.push(i)

    print(ll)
    print(palindrome(ll.head))
