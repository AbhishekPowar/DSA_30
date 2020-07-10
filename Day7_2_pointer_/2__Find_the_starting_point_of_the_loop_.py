# https://leetcode.com/problems/linked-list-cycle-ii/submissions/
# 2__Find_the_starting_point_of_the_loop_


def detectCycle(self, head: ListNode) -> ListNode:
    if not head:
        return head
    slow = head
    fast = slow.next
    while slow != fast:
        slow = slow.next
        if fast and fast.next:
            fast = fast.next.next
        else:
            return None

    slow = head
    fast = fast.next
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast
