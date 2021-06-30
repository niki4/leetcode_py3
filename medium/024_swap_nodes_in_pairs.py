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
from tools.linked_list import ListNode


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

        
class Solution2:
    """
    LC recursion solution.
    Runtime: 24 ms, faster than 95.14% of Python3.
    Memory Usage: 14.1 MB, less than 99.98% of Python3.
    
    Time Complexity: O(N) where N is the size of the linked list.
    Space Complexity: O(N) stack space utilized for recursion.
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # nodes to be swapped
        first = head
        second = head.next
        
        # swapping
        first.next = self.swapPairs(second.next)
        second.next = first
        
        # now the head is the swapping node
        return second

    
class Solution3:
    """
    LC iterative solution.
    Runtime: 28 ms, faster than 83.37% of Python3.
    Memory Usage: 14 MB, less than 99.98% of Python3.
        
    Time Complexity: O(N) where N is the size of the linked list.
    Space Complexity: O(1).
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # dummy node acts as a prevNode for the head node 
        # of the list and hence and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head
        
        prev_node = dummy
        
        while head and head.next:
            # nodes to be swapped
            first = head
            second = head.next
            
            # swapping
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            # reinit the head and prev_node for the next swap
            prev_node = first
            head = first.next
        
        # return new head node
        return dummy.next
