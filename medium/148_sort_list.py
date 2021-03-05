"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logN) time and O(1) memory (i.e. constant space)?

Example 1:
    Input: head = [4,2,1,3]     4->2->1->3
    Output: [1,2,3,4]           1->2->3->4

Constraints:
    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105
"""
from problems.tools.linked_list import ListNode, make_linked_list_from_iterable, traverse


class Solution:
    """
    Bruteforce approach - traverse source linked list for values, then sort values, then rebuild new linked list

    Runtime: 220 ms, faster than 88.93% of Python3
    Memory Usage: 38.2 MB, less than 12.86% of Python3

    Time complexity: O(2*n)
    Space complexity: O(n)
    """

    def sortList(self, head: ListNode) -> ListNode:
        values = list()
        node = head
        while node:
            values.append(node.val)
            node = node.next
        values.sort()

        dummy_node = ListNode()
        prev = dummy_node
        for v in values:
            prev.next = ListNode(val=v)
            prev = prev.next
        return dummy_node.next


class Solution2:
    """
    Algorithm: Bottom Up Merge Sort
        1) Start with splitting the list into sublists of size 1. Each adjacent pair of sublists of size 1 is merged in
         sorted order. After the first iteration, we get the sorted lists of size 2. A similar process is repeated for
         a sublist of size 2. In this way, we iteratively split the list into sublists of size 1,2,4,8.. and so on
         until we reach n.

        2) To split the list into two sublists of given size beginning from start, we use two pointers, "mid" and "end"
        that references to the start and end of second linked list respectively. The split process finds the middle of
        linked lists for the given size.

    Runtime: 512 ms, faster than 38.93% of Python3
    Memory Usage: 30.2 MB, less than 40.20% of Python3

    Time Complexity: (n logN), where n is the number of nodes in linked list.
    Space Complexity: O(1), we use only constant space for storing the reference pointers tail, nextSubList etc.
    """

    def get_size(self, head: ListNode) -> int:
        """ Count the length of the linked list """
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter

    def split(self, head: ListNode, size: int) -> ListNode or None:
        """ Given the head & size, return the start node of the next chunk"""
        for i in range(size - 1):
            if not head:
                break
            head = head.next

        if not head:
            return None
        next_start, head.next = head.next, None  # disconnect

        return next_start

    def merge(self, l1: ListNode, l2: ListNode, dummy_start: ListNode):
        """ Given dummy_start, merge two lists and return the tail of merged list """
        curr = dummy_start
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        while curr.next:  # find tail node (which has .next=None)
            curr = curr.next
        return curr  # returned tail is the "dummy_start" node of next chunk

    def sortList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        total_length = self.get_size(head)
        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < total_length:
            dummy_start = dummy
            start = dummy.next
            while start:
                left = start
                right = self.split(left, size)  # start from left, cut with size=size
                start = self.split(right, size)  # start from right, cut with size=size
                dummy_start = self.merge(left, right, dummy_start)  # returned tail = next dummy_start
            size *= 2
        return dummy.next


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
    )
    for s in solutions:
        for inp, exp in tc:
            res = s.sortList(make_linked_list_from_iterable(inp))
            assert traverse(res) == exp, f"{s.__class__.__name__}: expected {exp}, got {traverse(res)}"
