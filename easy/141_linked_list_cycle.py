"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then
there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the second node.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    Runtime: 40 ms, faster than 84.74% of Python.
    Memory Usage: 18.7 MB, less than 15.15% of Python.

    Using hash set to check whether a node has been visited before.
    Runtime complexity: O(n)
    Space complexity: O(n)
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        node = head
        seen_before = set()

        while node:
            if node in seen_before:
                return True
            else:
                seen_before.add(node)
            node = node.next
        return False


class Solution2:
    """
    Runtime: 44 ms, faster than 65.63% of Python.
    Memory Usage: 18.5 MB, less than 21.46% of Python.

    Algorithm idea:
        Consider a cyclic list and imagine the slow and fast pointers
        are two runners racing around a circle track. The fast runner will
        eventually meet the slow runner. Why? Consider this case (we name it
        case A) - The fast runner is just one step behind the slow runner.
        In the next iteration, they both increment one and two steps
        respectively and meet each other.
    """
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()

    ln1 = ListNode(3)
    ln2 = ListNode(2)
    ln3 = ListNode(0)
    ln4 = ListNode(-4)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln2
    assert s.hasCycle(ln1) == True
    assert s2.hasCycle(ln1) == True

    head = ListNode(1)
    assert s.hasCycle(head) == False
    assert s2.hasCycle(head) == False
