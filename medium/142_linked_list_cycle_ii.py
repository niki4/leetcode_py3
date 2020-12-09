"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node that
tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 48 ms, faster than 77.02% of Python3
    Memory Usage: 17.7 MB, less than 6.95% of Python3

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        if not head: return

        node = head
        while node:
            if node in seen:
                return node
            seen.add(node)
            node = node.next
        return None  # no cycle


class Solution2:
    """
    Runtime: 52 ms, faster than 50.83% of Python3
    Memory Usage: 17.2 MB, less than 24.96% of Python3

    Time complexity: O(n)
    Space complexity: O(1)

    Algorithm: "Floyd's Tortoise and Hare" https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
    First we define if there an intersection point for slow (1 step at a time) and fast (2 steps at a time) pointers.
    Using that intersection point and a new one (starting from head) we need to step slowly (by 1 step) each ptr to get
    the node where the cycle begins.
    """

    def get_slow_and_fast_meeting_node(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        first = self.get_slow_and_fast_meeting_node(head)
        if not first:
            return

        second = head
        while first != second:
            first = first.next
            second = second.next
        return first


if __name__ == '__main__':
    # cycled list
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l2.next = l1
    sol = Solution()
    sol2 = Solution2()
    assert sol.detectCycle(l1) == l1
    assert sol2.detectCycle(l1) == l1

    # not cycled list
    l3 = ListNode(3)
    l4 = ListNode(4)
    l3.next = l4
    assert sol.detectCycle(l3) is None
    assert sol2.detectCycle(l3) is None
