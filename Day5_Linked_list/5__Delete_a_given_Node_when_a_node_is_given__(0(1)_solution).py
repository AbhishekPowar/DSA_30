# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/
# 5__Delete_a_given_Node_when_a_node_is_given__(0(1)_solution)
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like following:

# Example 1:

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


def deleteNode(self, node):

    node.val = node.next.val
    node.next = node.next.next
