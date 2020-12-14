"""
Given the head of a linked list, rotate the list to the right by k places.

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
"""
from collections import deque
from problems.tools.linked_list import make_linked_list_from_iterable, traverse


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Bruteforce solution using deque for storing and rotating values.
    """

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        values = deque()
        node = head
        while node:
            values.append(node.val)
            node = node.next

        shift = k % len(values)
        values.rotate(shift)

        node = head
        for v in values:
            node.val = v
            node = node.next
        return head


if __name__ == '__main__':
    solutions = [Solution()]
    tc = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
    ]
    for sol in solutions:
        for inp, rotate_count, exp in tc:
            inp_head = make_linked_list_from_iterable(inp)
            res = sol.rotateRight(inp_head, rotate_count)
            assert traverse(res) == exp, f'Want {exp}, got {traverse(res)}'
