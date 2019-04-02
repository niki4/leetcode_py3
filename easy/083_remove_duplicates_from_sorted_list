"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Runtime: 48 ms, faster than 81.82% of Python3.
Memory Usage: 13.1 MB, less than 5.26% of Python3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        
        while current is not None:
            if previous is None:
                previous = current
                current = current.next
                continue
            if current.val == previous.val:
                previous.next = current.next
                current = previous.next
            else:
                previous = current
                current = current.next
        
        return head
