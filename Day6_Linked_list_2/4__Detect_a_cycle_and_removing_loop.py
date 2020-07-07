# 4__Detect_a_cycle_and_removing_loop(two_different_questions_and_same_concept)

from dataStructure.linkedList import singlyLinkedList as sLL, Node


def hasCycle(head):
    node = head
    if node:
        slow = node
        fast = slow.next
        while slow != fast:
            slow = slow.next
            if fast:
                fast = fast.next
            else:
                return False

            if fast:
                fast = fast.next
            else:
                return False
        return True

    return False


def whereIsLoop(node):
    if node:
        count = 0
        slow = node
        fast = slow.next
        while slow != fast:
            count += 1
            slow = slow.next
            if fast:
                fast = fast.next
            else:
                return None

            if fast:
                fast = fast.next
            else:
                return None
        slow = node
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None


def removeLoop(node):
    if node:
        slow = node
        fast = slow.next
        while slow != fast:
            slow = slow.next
            if fast:
                fast = fast.next
            else:
                return node
            if fast:
                fast = fast.next
            else:
                return node

        slow = node
        while slow != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        return node
    return node


def makeLoop(node, loopat):
    # Creating Loop
    if node:
        temp = node
        count = 0
        while temp.next != None:
            if count == loopat:
                loop = temp
            temp = temp.next
            count += 1
        temp.next = loop
        return node
    return node


if __name__ == "__main__":
    n = 4

    # Pushing data
    ll = sLL()
    for i in range(1, n+1):
        ll.push(i)

    # Creating a loop
    # ll.head = makeLoop(ll.head, loopat=1)

    print('Linked list init:', ll)

    # Cycle check bool
    isPresent = hasCycle(ll.head)
    print(f'Loop is  present {isPresent}')

    # cycle check return start of loop
    ans = whereIsLoop(ll.head)
    print('Loop starts at ', ans)

    removeLoop(ll.head)
    print(f'Linked lis after loop removal', ll)
