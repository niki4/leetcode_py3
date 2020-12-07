"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation:
You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    The 'challenge' here is to keep link from previous node to the 'removed' one while having no access to the head
     (so we wouldn't traverse from the head). To satisfy this, instead of removing the node given in parameter, we
     just jump over the element next after given one, but copying its value and link to the next node.

    Runtime: 36 ms, faster than 81.47% of Python3
    Memory Usage: 14.8 MB, less than 15.73% of Python3
    Time and Space complexity: O(1)
    """

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
