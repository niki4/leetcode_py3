"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""
from tools.linked_list import ListNode, get_linked_list_representation


class Solution:
    """
    Runtime: 36 ms, faster than 96.32% of Python3.
    Memory Usage: 14.4 MB, less than 72.88% of Python3.

    Iterative approach.

    Runtime complexity: O(n)
    Space complexity: O(1)
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev  # the last node is the new head


class Solution2:
    """
    Runtime: 28 ms, faster than 53.93% of Python.
    Memory Usage: 18.5 MB, less than 5.04% of Python.

    Recursive approach.
    """

    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if node is None:
            return prev

        curr, node.next = node.next, prev
        return self._reverse(curr, node)


class Solution3:
    """
    Recursive approach.
    
    The recursive version key is to work backwards. 
    Assume that the rest of the list had already been reversed, now how do I reverse the front part? 
    Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

    Assume from node nk+1 to nm had been reversed and you are at node nk.
    n1 → … → nk-1 → nk → nk+1 ← … ← nm

    We want nk+1’s next node to point to nk.

    So, nk.next.next = nk;
    
    Runtime: 32 ms, faster than 86.81% of Python3
    Memory Usage: 18.7 MB, less than 7.97% of Python3 
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


class Solution4:
    """
    Algorithm idea: keep track of original head moving toward the other end while creating a new head at each iteration.
    So that for the original list 1->2->3->4->5->NULL with head "1" iterations will be as below
    2->1->->3->4->5->NULL
    3->2->1->->->4->5->NULL
    4->3->2->1->->->->5->NULL
    5->4->3->2->1->->->->->NULL

    Runtime: 36 ms, faster than 62.97% of Python3
    Memory Usage: 15.6 MB, less than 35.51% of Python3
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        # head is the original head and curr_head is the new head
        curr_head = head
        while head and head.next:
            node = head.next  # remember node
            head.next = node.next  # jump original head link over node
            node.next = curr_head
            curr_head = node  # set new head
        return curr_head


if __name__ == "__main__":
    def create_linked_list() -> ListNode:
        ln1 = ListNode(1)
        ln2 = ListNode(2)
        ln3 = ListNode(3)
        ln1.next = ln2
        ln2.next = ln3
        return ln1


    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    for s in solutions:
        head = create_linked_list()
        assert get_linked_list_representation(head) == '1 -> 2 -> 3'
        new_head = s.reverseList(head)
        assert get_linked_list_representation(new_head) == '3 -> 2 -> 1'
