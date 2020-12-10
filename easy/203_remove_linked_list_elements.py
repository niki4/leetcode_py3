"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
from problems.tools.linked_list import ListNode, get_linked_list_representation, make_linked_list_from_iterable


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return

        prev = None
        node = head

        while node:
            if node.val == val:
                if node == head:  # head
                    head = node.next
                    node = head
                elif node.next is None:  # tail
                    prev.next = None
                    return head
                else:  # somewhere in between
                    prev.next = node.next
                    node = prev.next
            else:
                prev = node
                node = node.next
        return head


if __name__ == '__main__':
    head_node = make_linked_list_from_iterable([1, 2, 6, 3, 4, 5, 6])  # 1->2->6->3->4->5->6
    sol = Solution()
    sol.removeElements(head_node, 6)
    assert get_linked_list_representation(head_node) == '1 -> 2 -> 3 -> 4 -> 5'
