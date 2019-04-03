"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Runtime: 48 ms (Your runtime beats 97.38 % of python3 submissions.)
Status: Accepted (https://leetcode.com/submissions/detail/149845717/)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode([1, 2, 3])
    l2 = ListNode([4, 5, 6])
    print(sol.mergeTwoLists(l1, l2))
