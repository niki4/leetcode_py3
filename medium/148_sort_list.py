"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logN) time and O(1) memory (i.e. constant space)?

Example 1:
    Input: head = [4,2,1,3]     4->2->1->3
    Output: [1,2,3,4]           1->2->3->4

Constraints:
    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105
"""
from problems.tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


class Solution:
    """
    Bruteforce approach - traverse source linked list for values, then sort values, then rebuild new linked list

    Runtime: 220 ms, faster than 88.93% of Python3
    Memory Usage: 38.2 MB, less than 12.86% of Python3

    Time complexity: O(2*n)
    Space complexity: O(n)
    """

    def sortList(self, head: ListNode) -> ListNode:
        values = list()
        node = head
        while node:
            values.append(node.val)
            node = node.next
        values.sort()

        dummy_node = ListNode()
        prev = dummy_node
        for v in values:
            prev.next = ListNode(val=v)
            prev = prev.next
        return dummy_node.next


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.sortList(make_linked_list_from_iterable(inp))
            assert traverse(res) == exp, f"{s.__class__.__name__}: expected {exp}, got {traverse(res)}"
