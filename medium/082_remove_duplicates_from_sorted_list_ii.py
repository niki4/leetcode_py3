"""
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3

Runtime: 52 ms, faster than 57.61% of Python3.
Memory Usage: 13.2 MB, less than 5.75% of Python3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def find_duplicated_items(self):
        prev = None
        curr = self.head
        duplicates = list()
        
        while curr is not None:
            if prev is None:
                prev = curr
                curr = curr.next
                continue
            if curr.val == prev.val:
                if curr.val not in duplicates:
                    duplicates.append(curr.val)
            prev = curr
            curr = curr.next
        return duplicates
    
    def delete_items_by_value(self, dup_values):
        prev = None
        curr = self.head
        
        while curr is not None:
            if curr.val in dup_values:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.head = head
        
        items_to_remove = self.find_duplicated_items()
        self.delete_items_by_value(items_to_remove)
        
        return self.head
