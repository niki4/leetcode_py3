"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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

        Recursive approach
        Runtime: 28 ms, faster than 97.91% of Python3.
        Memory Usage: 14.2 MB, less than 100.00% of Python3.
        Status: Accepted (https://leetcode.com/submissions/detail/149845717/)
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


class Solution2:
    """
    Iterative LC approach
    Runtime: 40 ms, faster than 43.70% of Python3.
    Memory Usage: 14.1 MB, less than 100.00% of Python3.
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prevhead = ListNode(-1)

        prev = prevhead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 or l2
        return prevhead.next


if __name__ == '__main__':
    sol1 = Solution()
    sol2 = Solution2()
    l1 = ListNode([1, 2, 3])
    l2 = ListNode([4, 5, 6])
    print(sol1.mergeTwoLists(l1, l2))
    print(sol2.mergeTwoLists(l1, l2))
