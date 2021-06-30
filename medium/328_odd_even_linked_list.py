"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Constraints:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""
from tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


class Solution:
    """
    Bruteforce approach with extra memory.

    Runtime: 44 ms, faster than 54.21% of Python3
    Memory Usage: 16.4 MB, less than 20.95% of Python3

    Time complexity: O(n)
    Space complexity: O(n) for storing odd and even values in regular list
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        node_idx = 1
        node = head

        even_values, odd_values = [], []

        while node:
            if node_idx % 2 == 0:
                even_values.append(node.val)
            else:
                odd_values.append(node.val)
            node = node.next
            node_idx += 1

        odd_values.extend(even_values)
        node = head
        for v in odd_values:  # odd values followed by even ones
            node.val = v
            node = node.next

        return head


class Solution2:
    """
    Algorithm idea: relink nodes while you traverse the initial list,
    so that odd-idx nodes will be linked with the odd ones,
    and the even-idx nodes are linked with the even ones.

    Runtime: 40 ms, faster than 79.14% of Python3
    Memory Usage: 16.3 MB, less than 27.86% of Python3

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next  # make link from one odd to another odd
            odd = odd.next  # switch odd to next odd one (for next iteration)
            even.next = odd.next  # make link from even to next even too
            even = even.next  # switch even to next even one (for next iteration)

        # now odd is the tail of list of odd-idx items. Simply extend it with the even-idx list using its head.
        odd.next = even_head
        return head


if __name__ == '__main__':
    def get_tc():
        return [
            ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
            ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
        ]


    solutions = [Solution(), Solution2()]
    for s in solutions:
        for inp, exp in get_tc():
            res = s.oddEvenList(make_linked_list_from_iterable(inp))
            assert traverse(res) == exp, f'\nInput:\t\t{inp}\nResult:\t\t{traverse(res)}\nExpected:\t{exp}'
