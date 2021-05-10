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


class Solution2:
    """
    We may convert binary representation to base10 by taking into account shift of each digit.
    So that moving from right to left numerical place will adds 2**i to each bit where i started from 0 (growing by 1
    at each shift left).

    Albeit we traversing list from head toward its tail (so reading binary number from left to right), we do sum of all
    "curr_bit_val * 2**i" so the result will be the same in both cases.

    For example:
    101 (base2) == (1 * 2**0) + (0 * 2**1) + (1 * 2**2) == (1 * 1) + (0 * 2) + (1 * 4) == 5 (base10)

    Runtime: 28 ms, faster than 83.64% of Python3
    Memory Usage: 14.3 MB, less than 38.29% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        node = head
        while node:
            num = num * 2 + node.val
            node = node.next
        return num


class Solution3:
    """
    The same idea as in Solution2, but using bitwise operators which are generally faster.

    Instead "num = num * 2 + x" at each node we using "num = (num << 1) | x" to get the same result.
    Computation for conversion 101 (base2) to 5 (base10), step by step:
    num = (0 << 1) | 1 == 0 | 1 == 1
    num = (1 << 1) | 0 == 2 | 0 == 2
    num = (2 << 1) | 1 == 4 | 1 == 5

    Runtime: 28 ms, faster than 83.64% of Python3
    Memory Usage: 14.1 MB, less than 88.88% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        node = head
        while node:
            num = (num << 1) | node.val
            node = node.next
        return num


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
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
            res = sol.getDecimalValue(ll_head)
            assert res == exp_base10_int, f"expected {exp_base10_int}, got {res}"
