"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
    (1) -> (0) -> (1)
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10

Constraints:
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
"""

from tools.linked_list import ListNode, make_linked_list_from_iterable


class Solution:
    """
    Runtime: 28 ms, faster than 83.64% of Python3
    Memory Usage: 14.1 MB, less than 68.95% of Python3

    Time / Space complexity: O(n)
    """

    def getDecimalValue(self, head: ListNode) -> int:
        digits = []
        node = head
        while node:
            digits.append(str(node.val))
            node = node.next
        return int("".join(digits), base=2)


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 0, 1], 5),
        ([0], 0),
        ([1], 1),
        ([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 18880),
        ([0, 0], 0),
    )
    for sol in solutions:
        for ll_values, exp_base10_int in tc:
            ll_head = make_linked_list_from_iterable(ll_values)
            assert sol.getDecimalValue(ll_head) == exp_base10_int
