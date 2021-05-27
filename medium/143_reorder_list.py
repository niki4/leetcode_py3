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


class Solution2:
    """
    Reverse the Second Part of the List and Merge Two Sorted Lists

    Use "hare & turtle (slow pointer & fast pointer)" approach to find the mid of the list.
    Then reverse second half of the list in place.
    Then merge list traversing from start (1st ptr) and mid (2nd ptr) nodes toward end (until the 2nd ptr reach end).

    Runtime: 84 ms, faster than 93.32% of Python3
    Memory Usage: 23.3 MB, less than 77.97% of Python3

    Time complexity: O(N)
    Space complexity: O(1)
    """

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # find the middle of linked list, e.g. for 1->2->3->4->5->6 it's 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # it'll be middle once fast == None
            fast = fast.next.next

        # reverse the second part of the list (starting from middle node) in place.
        # e.g. convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge two sorted lists
        # e.g., merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
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
