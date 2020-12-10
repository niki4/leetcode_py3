"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from problems.tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


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
                l1, l2 = l2, l1  # swap guarantees us l1 is always lowest (or eq) value element
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


class Solution3:
    """
    Bruteforce solution with O(2n+m) additional space for storing values / new list to return.
    Maybe good starting point for further optimization / more complicated logic.

    Runtime: 40 ms, faster than 38.87% of Python3
    Memory Usage: 14.4 MB, less than 7.85% of Python3
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_values = list()
        while l1:
            list_values.append(l1.val)
            l1 = l1.next
        while l2:
            list_values.append(l2.val)
            l2 = l2.next
        list_values.sort()

        head = None
        prev = None
        for v in list_values:
            node = ListNode(v)
            if not head:
                head = prev = node
            else:
                prev.next = node  # make link to the new node
                prev = node  # remember the new node for next iteration
        return head


if __name__ == '__main__':
    def get_tc():
        return [(
            make_linked_list_from_iterable([1, 2, 4]),
            make_linked_list_from_iterable([1, 3, 4]),
            make_linked_list_from_iterable([1, 1, 2, 3, 4, 4]),
        )]


    solutions = [Solution(), Solution2(), Solution3()]
    for s in solutions:
        print()
        for l1, l2, exp in get_tc():
            assert traverse(s.mergeTwoLists(l1, l2)) == traverse(exp), f'{s.__class__.__name__} test failed'
