"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 24 ms, faster than 99.56% of Python3.
    Memory Usage: 13.2 MB, less than 31.27% of Python3.

    Time complexity: O(n) as we need to traverse the linked list
    Space complexity: O(n) as we need additional storage to store our nodes in regular list
    """
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return

        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        center = len(nodes) // 2
        return nodes[center]


class Solution2:
    """
    Runtime: 32 ms, faster than 89.80% of Python3.
    Memory Usage: 13.1 MB, less than 72.35% of Python3.

    Algorithm idea:
        Use 2 pointers - slow and fast. Fast is twice faster than slow, therefore once the fast pointer
        reaches end of the list, we return the slow one (as it's the center)

    Time complexity: O(n) as we need to traverse the linked list
    Space complexity: O(1)
    """
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast is not None else slow


class Solution3:
    """
    Runtime: 36 ms, faster than 75.43% of Python3.
    Memory Usage: 13.2 MB, less than 52.45% of Python3.

    Shorter version of the Solution2.
    We don't use the separate slow pointer, but reuse the existing one that initialy pointed to the head.
    Yet we omit check whether slow pointer is not None as it will be always behind the fast one.
    """
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
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
    s3 = Solution3()

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
    assert s1.middleNode(head).val == 3
    assert s2.middleNode(head).val == 3
    assert s3.middleNode(head).val == 3

    ln5 = ListNode(6)
    ln4.next = ln5
    assert getSinglyLinkedListValues(head) == '1->2->3->4->5->6'
    assert s1.middleNode(head).val == 4
    assert s2.middleNode(head).val == 4
    assert s3.middleNode(head).val == 4
