"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 40 ms, faster than 75.77% of Python3.
    Memory Usage: 13.3 MB, less than 22.28% of Python3.

    Time complexity: O(3*n) - one pass to traverse 1st list, 2nd to rebuilt values arr, 3rd to create list
    Space complexity: O(2*n) as we need to store values from first list and to create another one
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return

        values = []
        new_head = point = ListNode(0)
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        del values[-n]
        for node_val in values:
            point.next = ListNode(node_val)
            point = point.next
        return new_head.next


class Solution2:
    """
    Runtime: 40 ms, faster than 75.77% of Python3.
    Memory Usage: 13.1 MB, less than 83.55% of Python3.
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


def getSinglyLinkedListValues(head: ListNode) -> str:
    """ Helper function that returns human friendly representation of Linked List values"""
    values = []
    node = head
    while node is not None:
        values.append(str(node.val))
        node = node.next
    return '->'.join(values)


if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution2()
    head = ListNode(1)
    ln1 = ListNode(2)
    ln2 = ListNode(3)
    ln3 = ListNode(4)
    ln4 = ListNode(5)
    head.next = ln1
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    assert getSinglyLinkedListValues(head) == '1->2->3->4->5'
    new_list_head = s1.removeNthFromEnd(head, 2)
    assert getSinglyLinkedListValues(new_list_head) == '1->2->3->5'
    new_list_head2 = s2.removeNthFromEnd(new_list_head, 2)
    assert getSinglyLinkedListValues(new_list_head2) == '1->2->5'
