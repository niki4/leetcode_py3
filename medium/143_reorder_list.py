"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000
"""

from tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


class Solution:
    """
    Runtime: 96 ms, faster than 44.50% of Python3
    Memory Usage: 23.6 MB, less than 9.32% of Python
    """

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        rev_nodes = nodes[int(len(nodes) / 2):]
        node = head
        while rev_nodes:
            rev_node = rev_nodes.pop()
            if rev_node == node:  # last item already in place, special case for odd-length lists
                break
            temp = node.next
            rev_node.next = node.next
            node.next = rev_node
            node = temp
        node.next = None  # unbind last node ref to break cycle


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    )
    for sol in solutions:
        for inp_list, out_list in tc:
            head_ = make_linked_list_from_iterable(inp_list)
            sol.reorderList(head_)
            reordered_list = traverse(head_)
            assert reordered_list == out_list, f"{sol.__class__.__name__}: expected {out_list}, got {reordered_list}"
