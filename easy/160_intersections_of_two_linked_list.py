"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Input:
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,0,1,8,4,5]
    skipA = 2
    skipB = 3
Output: Reference of the node with value = 8
Input Explanation:
    The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected
    node in B.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Runtime: 228 ms, faster than 21.28% of Python.
    Memory Usage: 42.3 MB, less than 6.25% of Python.

    Runtime complexity: O(m + n) as we need to traverse both lists, O(1) for lookup in hash set
    Space complexity: O(n) as we need to store values from listA
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return

        listA_nodes = set()

        nodeA = headA
        nodeB = headB

        while nodeA is not None:
            listA_nodes.add(nodeA)
            nodeA = nodeA.next

        while nodeB is not None:
            if nodeB in listA_nodes:
                return nodeB
            nodeB = nodeB.next

class Solution2:
    """
    Runtime: 200 ms, faster than 78.53% of Python.
    Memory Usage: 41.8 MB, less than 40.72% of Python.

    Algorithm idea:
    1. Maintain two pointers pA and pB initialized at the head of A and B, respectively.
    Then let them both traverse through the lists, one node at a time.
    2. When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right);
    similarly when pB reaches the end of a list, redirect it the head of A.
    3. If at any point pA meets pB, then pA/pB is the intersection node and we
    return either one of them. It will works also in case if no intersections, so there
    will be ptrA == ptrB == None and we will exit the while loop.

    Yet, We dont really need to compare if headA is None or headB is None (as on begin of Solution1).
    If A and B are both None, we just return one of them. If only one of them is None,
    they will go into the while loop just like all the other linked lists that dont meet each other.
    """
    def getIntersectionNode(self, headA, headB):
        ptrA = headA
        ptrB = headB

        while ptrA is not ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()

    head_a = ln1 = ListNode(0)
    ln2 = ListNode(1)
    ln3 = ListNode(2)
    head_b = ln4 = ListNode(3)
    ln1.next = ln2    # ln1--\
    ln2.next = ln3    #       -->ln2-->ln3
    ln4.next = ln2    # ln4--/
    assert s.getIntersectionNode(head_a, head_b).val == 1  # ln2 is intersection point, ln2.val==1
    assert s2.getIntersectionNode(head_a, head_b).val == 1
