"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    7 -> 2 -> 4 -> 3    l1
         5 -> 6 -> 4    l2
    7 -> 8 -> 0 -> 7    result

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

    Follow up: Could you solve it without reversing the input lists?
"""
from tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


class Solution:
    """
    Intuitive approach: collect values first, then sum digits in reverse order from both lists.
    Take carry number in mind for those sums that equal or exceed 10.
    Continue moving from least to most significant digits in both lists.
    Result reversed before return.

    Runtime: 68 ms, faster than 86.85% of Python3
    Memory Usage: 14.5 MB, less than 11.77% of Python3

    Time / Space complexity: O(n)
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_nums, l2_nums = [], []
        while l1:
            l1_nums.append(l1.val)
            l1 = l1.next
        while l2:
            l2_nums.append(l2.val)
            l2 = l2.next

        prev, head = None, None
        carry = 0
        while l1_nums or l2_nums or carry:
            a_val = l1_nums.pop() if l1_nums else 0
            b_val = l2_nums.pop() if l2_nums else 0
            c_sum = a_val + b_val + carry

            new_node = ListNode(c_sum % 10)  # num at node should be <= 9
            carry = c_sum // 10
            if not prev:
                prev = new_node
                head = prev
            else:
                prev.next = new_node
                prev = new_node
        sum_head = self.reverse_linked_list(head)
        return sum_head

    def reverse_linked_list(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
        ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
        ([0], [0], [0])
    )
    for sol in solutions:
        for a, b, expected_c in tc:
            a_list = make_linked_list_from_iterable(a)
            b_list = make_linked_list_from_iterable(b)
            c_arr = traverse(sol.addTwoNumbers(a_list, b_list))
            assert c_arr == expected_c
