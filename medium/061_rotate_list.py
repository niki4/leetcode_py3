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

    Runtime: 40 ms, faster than 40.17% of Python3
    Memory Usage: 14.3 MB, less than 10.84% of Python3
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


class Solution2:
    """
    Algorithm idea: close the ring once you reached the tail, at this point you will know the size of the list,
    then we calculate the shift to make a new tail (imagine list being rotated physically - tail will be moved as well)
    and a new head as a next node (after tail). The last step is to break the ring - just unlink new tail (set None).

    Runtime: 36 ms, faster than 71.20% of Python3
    Memory Usage: 14.3 MB, less than 27.22% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        len_values = 1
        node = head
        while node and node.next:
            len_values += 1
            node = node.next
        old_tail = node
        old_tail.next = head  # close the ring

        shift = len_values - (k % len_values) - 1
        node = head
        idx = 0
        while idx != shift:
            node = node.next
            idx += 1
        new_tail = node
        new_head = node.next
        new_tail.next = None  # break the ring
        return new_head


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
    ]
    for sol in solutions:
        for inp, rotate_count, exp in tc:
            inp_head = make_linked_list_from_iterable(inp)
            res = sol.rotateRight(inp_head, rotate_count)
            assert traverse(res) == exp, f'Want {exp}, got {traverse(res)}'
