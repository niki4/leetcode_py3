"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Runtime: 36 ms, faster than 80.68% of Python3.
    Memory Usage: 13.1 MB, less than 5.04% of Python3.
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head.next
            head.next, temp.next = self.swapPairs(temp.next), head
            return temp
        else:
            return head
