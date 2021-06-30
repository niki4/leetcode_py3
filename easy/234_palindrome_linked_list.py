"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
from tools.linked_list import ListNode, make_linked_list_from_iterable


class Solution:
    """
    Runtime: 72 ms, faster than 95.53% of Python3.
    Memory Usage: 24 MB, less than 21.89% of Python3.

    Runtime complexity: O(n). We have to visit all nodes.
    Memory complexity: O(n). We need additional storage for n values.
    """

    def isPalindrome(self, head: ListNode) -> bool:
        values = []

        while head is not None:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


class Solution2:
    """
    This solution requires us to (temporary) reverse half of the list to compare in order.

    Runtime complexity: O(n). We have to visit all nodes.
    Memory complexity: O(1). We are not using separate storage for nodes.
    """

    def isPalindrome(self, head: ListNode) -> bool:
        result = True
        if head is None:
            return result

        # Find the mid of the list (first half end) and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end)

        # Check whether it's a palindrome
        first_pos = head
        second_pos = second_half_start
        while first_pos and second_pos:
            if first_pos.val != second_pos.val:  # not a palindrome
                result = False
                break
            first_pos = first_pos.next
            second_pos = second_pos.next

        # Restore the list and return result
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


if __name__ == "__main__":
    solutions = [Solution(), Solution2()]
    tc = [
        (make_linked_list_from_iterable([1, 2, 2, 1]), True),  # palindrome_list
        (make_linked_list_from_iterable([1, 2]), False),  # non_palindrome_list
    ]
    for s in solutions:
        for inp, exp in tc:
            assert s.isPalindrome(inp) == exp
